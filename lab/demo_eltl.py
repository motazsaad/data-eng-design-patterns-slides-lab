#!/usr/bin/env python3
"""
ETLT vs. ELTL pattern comparison demo

This script compares two pipeline definitions:
- ETL (Extract → Transform → Load)
- ETLT (Extract → Transform → Load → Transform)

It shows how ETLT++ adds governance, versioning, semantic-layer/semantic-curation obligations, and observability, and how data-quality gates (e.g. schema validation and thresholds) can be specified as pattern obligations.

Based on the ETLT/ELTL design pattern papers:
  C. Rucco, A. Longo, and M. Saad, "Enhancing data ingestion efficiency in cloud-based systems: A design pattern approach," Data Science and Engineering, vol. 11, pp. 287--302, 2026.
  C. Rucco, M. Saad, T. Martina, and A. Longo, "ETLT and ELTL as architectural patterns: an initial specification and enhanced variants," 2026.
"""

import csv
import json
from pathlib import Path

# Sample data for the demo
SAMPLE_CUSTOMERS = [
    {"id": "C001", "name": "Alice", "email": "alice@example.com", "country": "US"},
    {"id": "C002", "name": "Bob", "email": "bob@example.com", "country": "CA"},
    {"id": "C003", "name": "Carol", "email": "carol@example.com", "country": "US"},
]

# ETL pipeline: Extract → Transform → Load
ETL_PIPELINE = {
    "name": "etl",
    "stages": [
        {"stage": "extract", "action": "read_csv", "source": "customers.csv"},
        {"stage": "transform", "action": "clean_and_normalize"},
        {"stage": "load", "action": "insert_into_postgres", "target_table": "customers"},
    ],
}

# ETLT pipeline: Extract → Transform → Load → Transform (extra transform after load)
ETLT_PIPELINE = {
    "name": "eltlt",
    "stages": [
        {"stage": "extract", "action": "read_csv", "source": "customers.csv"},
        {"stage": "transform", "action": "clean_and_normalize"},
        {"stage": "load", "action": "insert_into_postgres", "target_table": "customers"},
        {"stage": "transform2", "action": "enrich_with_metadata", "target_table": "customers_enriched"},
    ],
}

# ETLT++ enhanced contract with versioning, semantic curation, and quality gates
ETLT_PLUS_PLUS_CONTRACT = {
    "name": "eltlt++",
    "description": "ETLT with explicit contracts, versioning, semantic curation, continuous monitoring",
    "schema_version": "v2.1",
    "stages": [
        {"stage": "extract", "action": "read_csv", "version": "v1", "contract": "source_schema"},
        {"stage": "transform", "action": "clean_and_normalize", "version": "v1", "contract": "clean_schema"},
        {"stage": "load", "action": "insert_into_postgres", "version": "v1", "target_table": "customers", "contract": "customers_schema"},
        {"stage": "transform2", "action": "enrich_with_metadata", "version": "v2", "target_table": "customers_enriched", "contract": "enrichment_contract"},
    ],
    "quality_gates": {
        "schema_validation": True,
        "row_count_threshold": 100,
        "null_percentage_threshold": 5.0,
    },
    "observability": {
        "metric_prefix": "eltlt",
        "export_backend": "prometheus",
    },
}


def print_pipeline(name, pipeline):
    print(f"\n--- {name.upper()} PIPELINE ---")
    for stage in pipeline["stages"]:
        stage_info = f"  {stage['stage']}: {stage['action']}"
        if "target_table" in stage:
            stage_info += f" → {stage['target_table']}"
        if "source" in stage:
            stage_info += f" from {stage['source']}"
        print(stage_info)


def print_contract(contract):
    print(f"\n--- {contract['name'].upper()} CONTRACT ---")
    print(f"  Description: {contract['description']}")
    if "schema_version" in contract:
        print(f"  Schema version: {contract['schema_version']}")
    if "stages" in contract:
        for stage in contract["stages"]:
            stage_info = f"    {stage['stage']}: {stage['action']}"
            if "version" in stage:
                stage_info += f" (v{stage['version']})"
            if "contract" in stage:
                stage_info += f" [{stage['contract']}]"
            if "target_table" in stage:
                stage_info += f" → {stage['target_table']}"
            print(stage_info)
    if "quality_gates" in contract:
        for gate, value in contract["quality_gates"].items():
            print(f"  Quality gate: {gate} = {value}")
    if "observability" in contract:
        for key, value in contract["observability"].items():
            print(f"  Observability: {key} = {value}")


print("ETL Pipeline:")
print_pipeline("etl", ETL_PIPELINE)

print("\nETLT Pipeline:")
print_pipeline("eltlt", ETLT_PIPELINE)

print("\nETLT++ Enhanced Contract:")
print_contract(ETLT_PLUS_PLUS_CONTRACT)