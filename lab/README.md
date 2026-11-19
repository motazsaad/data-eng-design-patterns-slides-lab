# Data Engineering Design Patterns — Hands-on Lab

> **3-hour tutorial only.** Supported operating systems: Linux, macOS, Windows 11 with WSL2.
> Required software: Python 3.10+, Docker (orchestrator services), Ollama (local LLM).
> Attendee equipment: laptop with $\geq$8\,GB RAM; a setup guide and pre-pulled Docker images will be provided in advance.

## Lab structure

The lab is modular and can be run in parts. Each demo takes 10–15 minutes.

### Demo 1 — MIND ingestion pattern
- **Goal:** Verify a metadata-driven ingestion pipeline that uses a catalog of connectors (declared as data, not code) and produces idempotent, resumable loads.
- **Steps:**
  1. A small JSON connector catalog is provided (3 sources: USGS, Open-Meteo, a custom CSV).
  2. A Python script reads the catalog and issues the appropriate ingestion commands.
  3. Run the pipeline twice to confirm idempotency (no duplicate records).
  4. Modify one record in the source and re-run to confirm resumability.
- **Outcome:** Attendees see how metadata-driven design reduces code duplication and enables portable pipelines.

### Demo 2 — ETLT vs. ELTL pattern comparison
- **Goal:** Compare stage orderings and observe the enhanced (++) variants that add governance, versioning, and observability.
- **Steps:**
  1. Two pipeline definitions are provided: one ETL and one ETLT (with an extra Transform step after Load).
  2. Execute both pipelines over the same input data and compare output records.
  3. Inspect the ETLT++ contract file (YAML) that specifies schema evolution rules and quality gates.
  4. Observe how the ++ variant flags a schema mismatch that the base ETL would silently accept.
- **Outcome:** Attendees experience how explicit contracts make pipelines more robust and governable.

### Demo 3 — EADF promotion simulation
- **Goal:** Simulate promoting a data pipeline across DEV $\rightarrow$ SIT $\rightarrow$ UAT $\rightarrow$ PROD using Environment-Aware Design Pattern (EADF) artifacts.
- **Steps:**
  1. A component definition YAML, an environment catalog YAML, and a pipeline template YAML are provided.
  2. A simple script performs "late binding": it merges the component with the target environment's catalog, resolving environment-specific connections (DB URLs, API keys, etc.).
  3. Run the script for each environment (DEV, SIT, UAT) and observe how bindings change.
  4. A schema evolution test: modify a field in the component and re-run to see how the promotion policy handles the change.
- **Outcome:** Attendees see how EADF eliminates environment-specific bugs and makes promotions reproducible and auditable.

### Demo 4 — LLM-generated pipeline + execution-based evaluation
- **Goal:** Generate an orchestrator-native pipeline artifact with a local LLM and score the data delivered to a sink.
- **Steps:**
  1. A pipeline task is described in natural language (e.g., "ingest USGS water level data, compute daily aggregates, sink to PostgreSQL").
  2. Using Ollama (local LLM), generate an Airflow DAG or n8n JSON workflow that attempts to fulfill the task.
  3. Deploy the generated artifact to a Dockerized orchestrator (provided image).
  4. Execute the pipeline with archived fixture data and compare the sink records against a reference output.
  5. Score the result: artifact error, execution error, or platform-specific issue.
- **Outcome:** Attendees experience the full cycle: LLM-generated $\rightarrow$ deployed $\rightarrow$ executed $\rightarrow$ scored, and learn the limitations of syntax-only validation.

## Lab debrief (3 h version, 10 min)
- Review scores and discuss common failure modes.
- Compare platform-specific behaviors (e.g., NiFi vs. Airflow).
- Pointers to the benchmark harness, fixtures, and reference artifacts.

## Prerequisites checklist (per attendee)
- [ ] Laptop with $\geq$8\,GB RAM, Docker running, Python 3.10+ installed
- [ ] Ollama pulled (instructions provided before tutorial)
- [ ] Pre-pulled Docker images (orchestrator services + evaluation harness)
- [ ] Optional: a favorite data engineering task to try with the LLM

## Lab files

| File | Description |
|---|---|
| `demo_mind.py` | Demo 1 — MIND metadata-driven ingestion (uses `connectors.json`, `metadata-table.csv`) |
| `demo_eltl.py` | Demo 2 — ETLT vs. ELTL pattern comparison (shows ETLT++ contract) |
| `demo_eadf.py` | Demo 3 — EADF environment-aware promotion simulation |
| `connectors.json` | Connector catalog for the MIND ingestion demo |
| `metadata-table.csv` | Metadata table (source, table, primary key, watermark, ingestion type) for the MIND demo |

## Run instructions

```bash
python3 demo_mind.py
python3 demo_eltl.py
python3 demo_eadf.py
```