#!/usr/bin/env python3
import csv
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "shark-navigator-filter-compatibility.csv"

def normalize(value):
    return "".join(value.upper().split()).replace("-", "")

def main():
    if len(sys.argv) != 2:
        print("Usage: python src/lookup.py MODEL_NUMBER")
        return 2
    query = normalize(sys.argv[1])
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        matches = [row for row in csv.DictReader(handle) if normalize(row["model_number"]) == query]
    if not matches:
        print("No exact match in this reference dataset.")
        return 1
    for row in matches:
        print(row["model_number"] + ": " + row["filter_kit"] + " — " + row["filter_type"])
        print("Source: " + row["official_source_url"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
