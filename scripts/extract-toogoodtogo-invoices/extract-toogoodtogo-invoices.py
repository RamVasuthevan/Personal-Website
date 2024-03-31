import os
import fitz  # PyMuPDF
import pprint as pp
import re
import yaml
from collections import OrderedDict
from datetime import datetime
import sys

# Specify the INVOICE_DIRECTORY containing the invoice PDF files
INVOICE_DIRECTORY = "/workspaces/Personal-Website/data/toogoodtogo/invoices"

# Specify the output YAML file
OUTPUT_FILE = "/workspaces/Personal-Website/website/_data/toogoodtogo.yml"


def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode("tag:yaml.org,2002:map", value)


yaml.add_representer(OrderedDict, represent_ordereddict)


def extract(file_path):
    """
    Extract text from a given PDF file
    :param file_path: Path to the file
    :return: Extracted text from the PDF file
    """
    extracted_text = ""
    # Check if it is a PDF file
    if file_path.endswith(".pdf"):
        try:
            # Open the PDF file
            with fitz.open(file_path) as pdf_file:
                # Loop through each page and extract text
                for page_num in range(len(pdf_file)):
                    page = pdf_file[page_num]
                    extracted_text += page.get_text()

        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
            raise e
    else:
        print(f"{file_path} is not a PDF file.")

    # Return the extracted text
    return extracted_text


def get_invoice_name(file_path, lines):
    invoice_name = os.path.splitext(os.path.basename(file_path))[0]

    assert re.match(
        r"^TGTG_\d+-\d+$", invoice_name
    ), f"Invalid invoice name {invoice_name} extracted from {file_path}"
    return invoice_name


def get_date(file_path, lines):
    date_str = lines[2][5:]

    if "/" in date_str:
        month, day, year = date_str.split("/")
        year = "20" + year if len(year) == 2 else year
        date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    assert re.match(
        r"^\d{4}-\d{2}-\d{2}$", date_str
    ), f"Invalid date {date_str} extracted from {lines[2]}"
    return date_str


def get_invoice_number(file_path, lines):
    invoice_number = lines[3][12:]

    assert re.match(
        r"^TGTG_\d+-\d+$", invoice_number
    ), f"Invalid invoice name {invoice_number} extracted from {lines[4]}"
    return invoice_number


def get_order_id(file_path, lines):
    order_id = lines[4][9:]

    assert len(order_id) == 11, f"Invalid order id {order_id} extracted from {lines[4]}"
    return order_id


def get_payment_method(file_path, lines):
    payment_method = [
        line for line in lines if line.startswith("This invoice has been paid with")
    ]

    assert (
        len(payment_method) == 1
    ), f"Invalid payment method {payment_method} extracted from {payment_method}"

    payment_method = payment_method[0][31:]
    if payment_method[0] == ":":
        payment_method = payment_method[1:]
    payment_method = payment_method.strip()

    return payment_method


def get_seller_name(file_path, lines):
    seller_name_idx = lines.index("Seller")
    seller_name = lines[seller_name_idx + 3]

    return seller_name


def get_hst_number(file_path, lines):
    hst_number_idx = lines.index("Seller") + 5

    if len(lines[hst_number_idx]) == 5:
        # hst_number_idx is a Zip Code and invoice is from the US
        assert (
            lines[hst_number_idx].isdigit() and len(lines[hst_number_idx]) == 5
        ), f"Invalid hst number {lines[hst_number_idx]} extracted from {lines[hst_number_idx]}"
        return None

    hst_number = lines[hst_number_idx]

    if hst_number == "HST:":
        # HST number is not on invice
        return None

    if hst_number.startswith("HST: "):
        hst_number = hst_number[5:]

    return hst_number


def get_store_name(file_path, lines):
    store_name_idx = lines.index("Seller")
    store_name = lines[store_name_idx + 2]

    return store_name


def get_store_address(file_path, lines):
    store_address_idx = lines.index("Seller")

    hst_number = bool(
        get_hst_number(file_path, lines) is not None
        or lines[store_address_idx + 5].startswith("HST:")
    )

    store_address_line_1 = lines[store_address_idx + 4]
    store_address_line_2 = lines[store_address_idx + 5 + int(hst_number)]
    store_address_line_3 = lines[store_address_idx + 6 + int(hst_number)]

    store_address = [store_address_line_1, store_address_line_2, store_address_line_3]
    return store_address


def get_hst_amount(file_path, lines):
    hst_amount = {}
    hst_amount_idx = [idx for idx, line in enumerate(lines) if line.startswith("HST,")]

    assert (
        len(hst_amount_idx) <= 1
    ), f"Invalid number of hst lines {len(hst_amount_idx)} extracted from {lines}"

    if len(hst_amount_idx) == 0:
        # HST amount is not on invoice
        return None

    hst_amount_line = lines[hst_amount_idx[0] + 1]

    assert re.match(
        r"\$\d+\.\d{2} \([A-Z]{3}\)", hst_amount_line
    ), f"Invalid hst amount {hst_amount_line} extracted from {lines}"

    hst_amount["amount"] = hst_amount_line[1:].split(" ")[0]  # format currency??
    hst_amount["currency"] = hst_amount_line[1:].split(" ")[1][1:-1]

    return hst_amount


def get_total(file_path, lines):
    total = {}

    total_idxs = [idx for idx, line in enumerate(lines) if line.startswith("Total")]

    assert (
        len(total_idxs) == 3
    ), f"Invalid number of total lines {len(total_idxs)} extracted from {lines}"

    total_line = lines[total_idxs[-1] + 1]

    assert re.match(
        r"\$\d+\.\d{2} \([A-Z]{3}\)", total_line
    ), f"Invalid total {total_line} extracted from {lines}"

    total["amount"] = total_line[1:].split(" ")[0]  # format currency??
    total["currency"] = total_line[1:].split(" ")[1][1:-1]

    return total


def get_items(file_path, lines):
    # Assuming one item on invoice
    items = []

    item_idx = lines.index("Description") + 7

    item = {}
    item["description"] = lines[item_idx + 1]
    item["quantity"] = lines[item_idx + 2]
    item["price"] = lines[item_idx + 3]
    total_line = lines[item_idx + 4]

    assert re.match(
        r"\$\d+\.\d{2} \([A-Z]{3}\)", total_line
    ), f"Invalid total {total_line} extracted from {lines}"

    item["total"] = {}
    item["total"]["amount"] = total_line[1:].split(" ")[0]  # format currency??
    item["total"]["currency"] = total_line[1:].split(" ")[1][1:-1]

    items.append(item)

    return items


def transform(file_path, text):
    lines = text.split("\n")

    details = {}
    details["invoice_name"] = get_invoice_name(file_path, text)
    details["date"] = get_date(file_path, lines)
    details["invoice_number"] = get_invoice_number(file_path, lines)
    details["order_id"] = get_order_id(file_path, lines)
    details["payment_method"] = get_payment_method(file_path, lines)
    details["seller_name"] = get_seller_name(file_path, lines)
    details["hst_number"] = get_hst_number(file_path, lines)
    details["seller_name"] = get_seller_name(file_path, lines)
    details["store_name"] = get_store_name(file_path, lines)
    details["store_address"] = get_store_address(file_path, lines)
    details["hst_amount"] = get_hst_amount(file_path, lines)
    details["total"] = get_total(file_path, lines)
    details["items"] = get_items(file_path, lines)

    return details


def create_yaml(details) -> str:
    # Define the order of the top-level fields
    field_order = [
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

    # Create an ordered dictionary from the detail dictionary
    ordered_details = OrderedDict()
    for field in field_order:
        if field not in details:  # Fail if a field is not found in details
            raise KeyError(f"Field {field} not found in details")

        value = details[field]
        if value is not None:  # Exclude fields that have None as a value
            ordered_details[field] = value

    # Dump the ordered dictionary to a YAML string
    yaml_str = yaml.dump(ordered_details, default_flow_style=False, sort_keys=False)

    return yaml_str


def load(details: dict, OUTPUT_FILE: str) -> None:
    details["description"] = ""
    details["notes"] = ""
    details["image"] = details["date"] + "/"
    details["hidden"] = True

    # Convert the detail dictionary to a YAML string
    yaml_str = create_yaml(details)

    # Check if the output file already exists, if not, create an empty list to hold the invoices
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as file:
            existing_invoices = yaml.safe_load(file) or []
    else:
        existing_invoices = []

    # Check if an invoice with the same invoice_name already exists in the list
    if any(
        invoice["invoice_name"] == details["invoice_name"]
        for invoice in existing_invoices
    ):
        print(
            f"Invoice with name {details['invoice_name']} already exists in {OUTPUT_FILE}"
        )
        return

    # Add the new invoice to the list
    existing_invoices.append(details)

    # Sort the invoices by date
    existing_invoices.sort(
        key=lambda invoice: datetime.strptime(invoice["date"], "%Y-%m-%d")
    )

    # Write the updated list of invoices back to the YAML file
    with open(OUTPUT_FILE, "w") as file:
        yaml.dump(existing_invoices, file, default_flow_style=False, sort_keys=False)


def process_invoices(invoice_file_paths: list, OUTPUT_FILE: str) -> None:
    for filepath in invoice_file_paths:
        # Check if the provided path is a valid file
        if not os.path.isfile(filepath) or not filepath.endswith(".pdf"):
            print(f"{filepath} is not a valid PDF file.")
            raise ValueError(f"{filepath} is not a valid PDF file.")

        # Process each invoice file
        try:
            extracted_text = extract(filepath)
            details = transform(filepath, extracted_text)
            load(details, OUTPUT_FILE)
        except Exception as e:
            print(f"Error processing {filepath}: {str(e)}")
            raise e


def list_files_in_invoice_directory(invoice_directory):
    # Collect all PDF files in the specified INVOICE_DIRECTORY
    try:
        invoice_file_paths = [
            os.path.join(invoice_directory, filename)
            for filename in os.listdir(invoice_directory)
            if os.path.isfile(os.path.join(invoice_directory, filename))
        ]
        return invoice_file_paths
    except FileNotFoundError as e:
        print(f"The invoice_directory {invoice_directory} does not exist.")
        raise e


if __name__ == "__main__":
    invoice_file_paths = list_files_in_invoice_directory(INVOICE_DIRECTORY)

    # Call the process_invoices function with the list of invoice file paths and the output file path
    process_invoices(invoice_file_paths, OUTPUT_FILE)
