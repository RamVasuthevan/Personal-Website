import importlib.util
import os
import unittest

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "extractor", os.path.join(SCRIPT_DIR, "extract-toogoodtogo-invoices.py")
)
extractor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractor)

EXTRACTED_FIELDS = [
    "invoice_name",
    "date",
    "invoice_number",
    "order_id",
    "payment_method",
    "seller_name",
    "hst_number",
    "store_name",
    "store_address",
    "hst_amount",
    "total",
    "items",
]


class TestExtractMatchesCommittedData(unittest.TestCase):
    def test_every_invoice_matches_committed_yaml(self):
        with open(extractor.DEFAULT_OUTPUT_FILE) as f:
            committed = {i["invoice_name"]: i for i in yaml.safe_load(f)}

        paths = extractor.list_files_in_INVOICE_DIRECTORY(
            extractor.DEFAULT_INVOICE_DIRECTORY
        )
        self.assertTrue(paths)

        for path in sorted(paths):
            name = os.path.splitext(os.path.basename(path))[0]
            if name not in committed:
                continue
            with self.subTest(invoice=name):
                details = extractor.transform(path, extractor.extract(path))
                for field in EXTRACTED_FIELDS:
                    self.assertEqual(
                        details.get(field), committed[name].get(field), field
                    )


if __name__ == "__main__":
    unittest.main()
