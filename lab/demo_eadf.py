#!/usr/bin/env python3
"""
EADF (Environment-Aware Design Pattern) promotion simulation demo

Simulates promoting a data pipeline across DEV → SIT → UAT → PROD
using environment-aware components with late binding.

Based on the EADF design pattern paper:
  C. Rucco, M. Saad, E. Puig, and A. Longo, "EADF: An Environment-Aware Deployment Design Pattern for Multi-Cloud Data Engineering CI/CD Pipelines," Research Square, 2025.
"""

import json
from pathlib import Path

# Component definition (template, environment-agnostic)
COMPONENT = {
    "name": "etl_pipeline_v1",
    "type": "data_pipeline",
    "source": "csv_files",
    "sink": "postgres",
    "version": "1.0.0",
    "description": "ETL pipeline for customer data ingestion",
    "transform_steps": [
        {"step": "extract", "script": "extract_customers.py"},
        {"step": "transform", "script": "transform_customers.sql"},
        {"step": "load", "script": "load_customers.py"},
    ],
}

# Environment catalog (defines environment-specific bindings)
ENVIRONMENT_CATALOG = {
    "DEV": {
        "source_path": "/tmp/data/dev/",
        "db_host": "localhost",
        "db_port": 5432,
        "db_name": "etl_dev",
        "credentials": "dev_credentials",
        "cloud_provider": "on-prem",
    },
    "SIT": {
        "source_path": "/data/sit/",
        "db_host": "sit-db.internal",
        "db_port": 5432,
        "db_name": "etl_sit",
        "credentials": "sit_credentials",
        "cloud_provider": "aws",
        "region": "eu-west-1",
    },
    "UAT": {
        "source_path": "/data/uat/",
        "db_host": "uat-db.internal",
        "db_port": 5432,
        "db_name": "etl_uat",
        "credentials": "uat_credentials",
        "cloud_provider": "azure",
        "region": "westeurope",
    },
    "PROD": {
        "source_path": "/data/prod/",
        "db_host": "prod-db.internal",
        "db_port": 5433,
        "db_name": "etl_prod",
        "credentials": "prod_credentials",
        "cloud_provider": "aws",
        "region": "eu-central-1",
    },
}

# Pipeline template (orchestrates stages)
PIPELINE_TEMPLATE = {
    "name": "etl_pipeline_template",
    "version": "1.0",
    "stages": [
        {"stage": "extract", "component": "etl_pipeline_v1", "params": {"source": "{source_path}/customers.csv"}},
        {"stage": "transform", "component": "etl_pipeline_v1", "params": {"script": "transform_customers.sql"}},
        {"stage": "load", "component": "etl_pipeline_v1", "params": {"table": "{db_name}.customers"}},
    ],
}

# Promotion policy
PROMOTION_POLICY = {
    "name": "etl_promotion_policy",
    "version": "1.0",
    "environments": ["DEV", "SIT", "UAT", "PROD"],
    "auto_promote": True,
    "approval_required": ["PROD"],
    "health_checks": {
        "row_count_diff_threshold": 0.05,
        "null_percentage_diff_threshold": 2.0,
        "schema_compatibility": "forward",
    },
}


def promote(component, environment):
    """Simulate late binding: merge component with target environment catalog."""
    env_config = ENVIRONMENT_CATALOG[environment]
    promoted = {
        **component,
        **env_config,
        "environment": environment,
        "deployed_at": "2023-01-01T00:00:00Z",
        "pipeline_template": PIPELINE_TEMPLATE,
        "promotion_policy": PROMOTION_POLICY,
    }
    return promoted


def simulate_promotion():
    """Simulate promoting the component through all environments."""
    environments = ["DEV", "SIT", "UAT", "PROD"]
    print("--- EADF PROMOTION SIMULATION ---")
    print(f"Component: {COMPONENT['name']} v{COMPONENT['version']}\n")

    for env in environments:
        promoted = promote(COMPONENT, env)
        print(f"Environment: {env}")
        print(f"  source_path: {promoted['source_path']}")
        print(f"  db_host: {promoted['db_host']}")
        print(f"  db_port: {promoted['db_port']}")
        print(f"  db_name: {promoted['db_name']}")
        print(f"  credentials: {promoted['credentials']}")
        print(f"  cloud_provider: {promoted['cloud_provider']}")
        if "region" in promoted:
            print(f"  region: {promoted['region']}")
        print()


if __name__ == "__main__":
    simulate_promotion()
    print("Late binding eliminates environment-specific bugs!")
    print("Promotion is reproducible and auditable across all environments.")