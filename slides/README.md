# Slides — A Data-Management Perspective on Data Engineering Design Patterns

Slide materials for the ICDE 2027 tutorial proposal **"A Data-Management Perspective on Data Engineering Design Patterns: Specifications, Semantics, and Execution-Based Evaluation"**.

## Contents

| File | Description |
|---|---|
| `tutorial-preview.tex` | Beamer source for the updated slide deck preview |
| `tutorial-preview.pdf` | Compiled slide deck preview |

## Topics covered

- Foundations, related-work positioning, and data-management semantics (exactly-once/at-least-once, idempotence, incremental loads, schema evolution, lineage/provenance)
- Ingestion patterns (MIND, cloud ingestion) with SESG ingestion-at-scale case study
- Transformation/architectural patterns (ETLT/ELTL, ETLT++/ELTL++), semantic-layer/semantic-curation obligations, and data-quality design patterns
- Environment-aware promotion in CI/CD (EADF)
- LLM-generated pipelines and execution-based, sink-level evaluation (Prefect & Kestra in hands-on lab)
- 3-hour two-slot structure, lab flow, and fallback path (hosted LLM endpoint + pre-generated/pre-computed artifacts)
- Open challenges and companion resources

## Build

Requires a LaTeX distribution with Beamer.

```bash
latexmk -pdf tutorial-preview.tex
```
