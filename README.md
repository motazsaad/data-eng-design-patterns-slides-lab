# Tutorial — A Data-Management Perspective on Data Engineering Design Patterns

Companion repository for the ICDE 2027 tutorial proposal
**"A Data-Management Perspective on Data Engineering Design Patterns: Specifications, Semantics, and Execution-Based Evaluation"**
by Motaz K. H. Saad, Chiara Rucco, and Antonella Longo (University of Salento).

## Overview

This tutorial surveys data engineering design patterns from a data-management perspective, framing patterns as explicit specifications whose obligations can be checked in LLM-generated, orchestrator-native pipelines via execution-based, sink-level scoring.

Topics covered:
- Foundations and related-work positioning for data engineering design patterns
- Core data-management semantics: exactly-once vs. at-least-once delivery, idempotence and incremental loads, schema evolution, and lineage/provenance
- Ingestion patterns (including metadata-driven MIND and cloud-based ingestion)
- Transformation and architectural patterns (ETLT/ELTL and enhanced variants), semantic-layer/semantic-curation obligations, and data-quality design patterns (profiling, validation, anomaly detection, issue triage, governed remediation)
- Environment-aware promotion in CI/CD (EADF)
- LLM-generated pipelines and execution-based evaluation across heterogeneous orchestrators
- Open challenges (pattern mining/validation/versioning, benchmark validity, governance, provenance, cost, human-in-the-loop)

## Repository contents

- `slides/tutorial-preview.tex`, `slides/tutorial-preview.pdf` — Beamer slide preview (also copied at repo root as `tutorial-preview.pdf`)
- `lab/` — Hands-on lab materials and demos:
  - `demo_mind.py` — metadata-driven ingestion demo (MIND)
  - `demo_eltl.py` — ETLT/ELTL and ETLT++ contract demo
  - `demo_eadf.py` — EADF environment-aware promotion demo
  - `connectors.json`, `metadata-table.csv` — fixtures for ingestion demo
  - `README.md` — lab setup, flow, and fallback instructions

## 3-hour hands-on lab (Slot 2)

- **Lightweight orchestrators:** Prefect and Kestra (containerized)
- **Flow:** select a task → generate an orchestrator-native artifact → deploy/run → score delivered sink records against a reference output
- **Local path (optional):** Python 3.10+, Docker, Ollama; laptop with ≥8 GB RAM recommended
- **Fallback path:** hosted LLM endpoint (OpenAI-compatible, session configuration provided) for artifact generation, plus pre-generated artifacts and pre-computed scoring outputs with optional instructor-hosted demo services
- Pre-pulled Docker images and cached models provided in advance; no-setup follow-along mode available for all attendees

## Related repositories

- MIND / ingestion design pattern: https://github.com/ChiaraRucco/DataEngDesignPattern_paper
- LLM-based pipeline generation: https://github.com/ChiaraRucco/LLM-pipeline-generation
- CI/CD design pattern validation (EADF): https://github.com/ChiaraRucco/CICD_DesignPattern_valuation
- Tutorial slides and hands-on lab (this repo): https://github.com/motazsaad/data-eng-design-patterns-slides-lab

## License

Open-source, Apache-2.0.
