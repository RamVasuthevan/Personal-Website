# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "openpyxl",
#   "requests"
# ]
# ///
#!/usr/bin/env python3
"""
Create Dem and Rep charts by race (2016–2024) from Pew validated voter tables. 
(Actual charts downloaded from https://chatgpt.com/g/g-p-67cdd0022e0c8191814638055c022bae/c/68aa16b7-3744-8330-9e98-6a8ce2a4df1e)

Usage:
  uv run make_charts.py
  uv run make_charts.py --input "/path/to/2016-2024 Validated Voter Detailed Tables.xlsx"
  uv run make_charts.py --dem-out dem-chart.png --rep-out rep-chart.png
"""

import argparse
import io
import os
import re
import sys
from typing import Dict

import pandas as pd
import requests
import matplotlib.pyplot as plt


DEFAULT_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/1JczVvbrlxkLiYYiNPSv0TRlWsbvYEihkZrnH1kQXIH8/edit"
)

RACES = ["White", "Black", "Hispanic", "Asian*"]

# We detect the correct columns by scanning the first rows for these strings.
COL_SIGNATURES = {
    "2016_Dem": "2016 Clinton vote",
    "2016_Rep": "2016 Trump vote",
    "2020_Dem": "2020 Biden vote",
    "2020_Rep": "2020 Trump vote",
    "2024_Dem": "2024 Harris vote",
    "2024_Rep": "2024 Trump vote",
}

SHEET_FUZZY_PREFIX = "2016-2024 Validated Voter Detai"  # first part of the Pew sheet name


def gsheets_to_export_url(url: str) -> str:
    """Turn a Google Sheets edit URL into a direct .xlsx export URL."""
    if "docs.google.com/spreadsheets" not in url:
        return url
    base = re.split(r"/edit.*", url)[0]
    return f"{base}/export?format=xlsx"


def load_dataframe(input_path_or_url: str | None) -> pd.DataFrame:
    """
    Load the workbook from local path or (default) Google Sheets URL.
    If no input is given or the input looks like a URL, we (re)download it.
    """
    # No path provided -> download from the default URL
    if not input_path_or_url:
        export_url = gsheets_to_export_url(DEFAULT_SHEET_URL)
        resp = requests.get(export_url)
        resp.raise_for_status()
        xls = pd.ExcelFile(io.BytesIO(resp.content))
    else:
        # If input looks like a URL (starts with http), download
        if str(input_path_or_url).startswith("http"):
            export_url = gsheets_to_export_url(str(input_path_or_url))
            resp = requests.get(export_url)
            resp.raise_for_status()
            xls = pd.ExcelFile(io.BytesIO(resp.content))
        else:
            # Treat as local file path
            if not os.path.exists(input_path_or_url):
                raise FileNotFoundError(f"File not found: {input_path_or_url}")
            xls = pd.ExcelFile(input_path_or_url)

    # Pick the sheet that starts with our known prefix, else first sheet
    sheet_name = next((s for s in xls.sheet_names if s.startswith(SHEET_FUZZY_PREFIX)), xls.sheet_names[0])
    return pd.read_excel(xls, sheet_name=sheet_name)


def find_columns(df: pd.DataFrame, signatures: Dict[str, str], scan_rows: int = 30) -> Dict[str, str]:
    """Find column names by searching the first `scan_rows` rows for signature substrings."""
    found: Dict[str, str] = {}
    for col in df.columns:
        vals = df[col].head(scan_rows).astype(str).tolist()
        joined = "\n".join(vals)
        for key, phrase in signatures.items():
            if key not in found and phrase in joined:
                found[key] = col

    missing = [k for k in signatures if k not in found]
    if missing:
        raise RuntimeError(f"Could not locate these columns: {missing}. Found mapping: {found}")
    return found


def build_table(df: pd.DataFrame, colmap: Dict[str, str]) -> pd.DataFrame:
    """Extract the rows for our RACES and assemble numeric columns for 2016/2020/2024 Dem & Rep."""
    key_col = df.columns[0]
    subset = df[df[key_col].isin(RACES)].copy()

    out = pd.DataFrame({
        "Race": subset[key_col].values,
        "2016_Dem": subset[colmap["2016_Dem"]].values,
        "2016_Rep": subset[colmap["2016_Rep"]].values,
        "2020_Dem": subset[colmap["2020_Dem"]].values,
        "2020_Rep": subset[colmap["2020_Rep"]].values,
        "2024_Dem": subset[colmap["2024_Dem"]].values,
        "2024_Rep": subset[colmap["2024_Rep"]].values,
    })

    for c in out.columns[1:]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


def plot_series(table: pd.DataFrame, party: str, outfile: str) -> None:
    """Plot Democratic or Republican vote share by race across 2016/2020/2024."""
    years = [2016, 2020, 2024]
    plt.figure(figsize=(10, 6))

    for _, row in table.iterrows():
        vals = [row[f"2016_{party}"], row[f"2020_{party}"], row[f"2024_{party}"]]
        plt.plot(years, vals, marker="o", label=f"{row['Race']} ({party})")
        for x, y in zip(years, vals):
            if pd.notna(y):
                plt.text(x, y + 1, f"{int(round(y))}", ha="center", fontsize=9)

    plt.title(f"{'Democratic' if party=='Dem' else 'Republican'} Vote Share by Race (2016–2024)")
    plt.xlabel("Election Year")
    plt.ylabel(f"Percent Voting {'Democratic' if party=='Dem' else 'Republican'} (%)")
    plt.ylim(0, 100)
    plt.xticks(years)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile, dpi=200)
    plt.close()


def main():
    ap = argparse.ArgumentParser(description="Create Dem and Rep charts by race (2016–2024) from Pew validated voters.")
    ap.add_argument("--input", help="Local XLSX path or Google Sheets URL (default: downloads the Pew sheet).", default=None)
    ap.add_argument("--dem-out", default="dem-chart.png", help="Output filename for Democratic chart")
    ap.add_argument("--rep-out", default="rep-chart.png", help="Output filename for Republican chart")
    args = ap.parse_args()

    try:
        df = load_dataframe(args.input)
        colmap = find_columns(df, COL_SIGNATURES, scan_rows=30)
        table = build_table(df, colmap)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    plot_series(table, "Dem", args.dem_out)
    plot_series(table, "Rep", args.rep_out)

    print("\nExtracted vote shares by race (Pew validated voters):\n")
    print(table.to_string(index=False))
    print(f"\nSaved charts: {args.dem_out}, {args.rep_out}")


if __name__ == "__main__":
    main()
