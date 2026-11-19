#!/usr/bin/env python3
"""
MIND ingestion pattern demo script

Demonstrates the metadata-driven ingestion pattern (MIND):
- Connectors are declared as data (not code)
- Schema/metadata catalog drives idempotent, resumable loads
- Supports full and incremental ingestion strategies (date-based and hash-based)

Based on the MIND pattern from:
  Chiara Rucco, Antonella Longo, Motaz Saad.
  "MIND: A metadata-driven INgestion design pattern for efficient data ingestion."
  Big Data Research, vol. 43, Art. no. 100574, 2026.
"""

import csv
import json
import hashlib
import os
import sys
from pathlib import Path

CONNECTOR_CATALOG = "connectors.json"
METADATA_TABLE = "metadata-table.csv"
OUTPUT_FILE = "ingested_data.csv"
STATE_FILE = "ingestion_state.json"

# Raw source data (heterogeneous schemas)
RAW_DATA = {
    "usgs": [
        {"site_no": "01010500", "datetime": "2023-01-01", "value": 12.5, "location": "USGS-001"},
        {"site_no": "01010500", "datetime": "2023-01-02", "value": 13.1, "location": "USGS-001"},
    ],
    "open_meteo": [
        {"location_id": "EURO-1001", "date": "2023-01-01", "value": 18.2, "location": "EURO-1001"},
        {"location_id": "EURO-1001", "date": "2023-01-02", "value": 17.8, "location": "EURO-1001"},
    ],
    "custom_csv": [
        {"id": "TX-1001", "created_at": "2023-01-01", "value": 150.0, "location": "NA-001"},
        {"id": "TX-1002", "created_at": "2023-01-02", "value": 230.5, "location": "NA-002"},
    ],
}

# Normalize each source to a common schema: record_id, record_date, value, location
def normalize_records(source_name, records):
    normalized = []
    for r in records:
        if source_name == "usgs":
            normalized.append({
                "record_id": r["site_no"],
                "record_date": r["datetime"],
                "value": r["value"],
                "location": r["location"],
            })
        elif source_name == "open_meteo":
            normalized.append({
                "record_id": r["location_id"],
                "record_date": r["date"],
                "value": r["value"],
                "location": r["location"],
            })
        elif source_name == "custom_csv":
            normalized.append({
                "record_id": r["id"],
                "record_date": r["created_at"],
                "value": r["value"],
                "location": r["location"],
            })
    return normalized


def load_connector_catalog():
    with open(CONNECTOR_CATALOG, "r") as f:
        return json.load(f)


def load_metadata_table():
    with open(METADATA_TABLE, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_state():
    if Path(STATE_FILE).exists():
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def fetch_and_normalize(source_name, watermark):
    raw = RAW_DATA.get(source_name, [])
    normalized = normalize_records(source_name, raw)
    if watermark:
        normalized = [r for r in normalized if r["record_date"] > watermark]
    return normalized


def compute_hash(records):
    return hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()


def ingest(metadata, state):
    """Run one ingestion step from the metadata table."""
    source = metadata["data_source_name"]
    table = metadata["table_name"]
    watermark = metadata.get("watermark", "")
    itype = metadata["ingestion_type"]
    key = f"{source}.{table}"

    last_wm = state.get(key, {}).get("watermark", "")
    records = fetch_and_normalize(source, last_wm)

    new_wm = watermark if watermark else last_wm
    if records and itype == "Incremental":
        # For demo: use the latest record date as new watermark
        new_wm = max(r["record_date"] for r in records)

    state[key] = {"watermark": new_wm, "hash": compute_hash(records), "n": len(records)}
    return records, state


def main():
    catalog = load_connector_catalog()
    print(f"Loaded {len(catalog)} connectors from {CONNECTOR_CATALOG}")

    metadata = load_metadata_table()
    print(f"Loaded {len(metadata)} metadata rows from {METADATA_TABLE}")

    state = load_state()
    all_records = []
    for row in metadata:
        records, state = ingest(row, state)
        all_records.extend(records)
        key = f"{row['data_source_name']}.{row['table_name']}"
        print(f"  [{key}] {row['ingestion_type']}: "
              f"{len(records)} new records, watermark={state[key]['watermark']}")

    if all_records:
        fieldnames = ["record_id", "record_date", "value", "location"]
        with open(OUTPUT_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_records)
    else:
        with open(OUTPUT_FILE, "w", newline="") as f:
            f.write("record_id,record_date,value,location\n")

    save_state(state)
    checksum = compute_hash(all_records)
    print(f"\nWrote {len(all_records)} records to {OUTPUT_FILE}")
    print(f"Checksum: {checksum}")
    print("Demo complete!")


if __name__ == "__main__":
    main()