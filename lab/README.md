# Hands-on Lab — A Data-Management Perspective on Data Engineering Design Patterns

Materials for the **3-hour tutorial** (Slot 2 lab, 45 min + 10 min debrief & Q&A).

## Lab goals

- Treat data-engineering patterns as **specifications** (forces, obligations, consequences)
- Generate orchestrator-native pipeline artifacts with an LLM
- Deploy and execute artifacts, then **score delivered sink records** against reference outputs (execution-based evaluation), checking obligations such as idempotency, schema/contract conformance, and quality gates

## Lightweight orchestrators (hands-on)

The guided lab uses **Prefect** and **Kestra** as lightweight, containerized orchestrators representative of the surveyed landscape (Airflow, n8n, Dagster, Prefect, NiFi, Kestra).

## Execution modes

### Local path (optional)
- **OS:** Linux, macOS, or Windows 11 with WSL2
- **Software:** Python 3.10+, Docker (Prefect/Kestra services and scoring harness), Ollama (local LLM)
- **Equipment:** laptop with ≥8 GB RAM recommended
- Pre-pulled Docker images and a lightweight cached model provided in advance; avoid downloads over conference Wi-Fi

### Fallback path (recommended if local resources are limited)
- **Hosted LLM endpoint** (OpenAI-compatible, session configuration provided) for artifact generation if local Ollama is unavailable or slow
- **Pre-generated artifacts** and **pre-computed scoring outputs**, with optional instructor-hosted demo services
- **No-setup follow-along mode** available for all attendees

## Lab flow (Prefect/Kestra)

1. **Select task and target:** choose a small pipeline task and target orchestrator (Prefect or Kestra)
2. **Generate artifact:** produce an orchestrator-native artifact (prompted generation via local Ollama or hosted LLM endpoint)
3. **Deploy/run:** run the artifact in the provided containerized environment
4. **Score:** compare delivered sink records to a reference output using the evaluation harness; classify outcomes (artifact/execution/platform/harness issues) and relate failures to pattern obligations

## Included demos (pattern foundations)

These runnable demos illustrate core patterns discussed in the tutorial and can be used as warm-up/reference exercises:

| Demo | File(s) | Focus |
|---|---|---|
| Metadata-driven ingestion (MIND) | `demo_mind.py`, `connectors.json`, `metadata-table.csv` | Connectors/metadata as data, idempotent/resumable/incremental loads |
| ETLT/ELTL and ETLT++ contract | `demo_eltl.py` | Stage ordering, contracts/versioning/quality gates/observability |
| EADF promotion (late binding) | `demo_eadf.py` | Environment-aware promotion across DEV/SIT/UAT/PROD |

### Run demos

```bash
python3 demo_mind.py
python3 demo_eltl.py
python3 demo_eadf.py
```

## Prefect/Kestra hands-on assets

Containerized Prefect/Kestra services, task prompts, reference outputs, and the scoring harness are provided with the lab setup package (pre-pulled images/configuration shared before the tutorial). Use the fallback pre-generated artifacts and pre-computed scores if you cannot run services locally.

## Debrief (10 min)

- Review scores and common failure modes (API misuse, platform-specific behavior, schema/contract mismatches)
- Discuss how execution-based scoring verifies pattern obligations (idempotency, schema evolution handling, quality gates, lineage-aware checks)
- Pointers to benchmark harness, fixtures, and companion repositories
