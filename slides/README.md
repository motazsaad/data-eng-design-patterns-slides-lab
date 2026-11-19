# Slides — Data Engineering Design Patterns Tutorial

This folder contains slide materials for the **Data Engineering Design Patterns** tutorial.

## Contents

| File | Description |
|---|---|
| `tutorial-preview.tex` | Beamer source for the slide deck preview |
| `tutorial-preview.pdf` | Compiled slide deck preview |

## Topics covered (preview)

- Foundations: what a design pattern is (POSA form, pattern language for data engineering)
- Ingestion patterns (e.g. MIND, cloud ingestion)
- Transformation and architectural patterns (ETLT/ELTL and variants)
- Environment-aware promotion in CI/CD (EADF)
- LLM-generated pipelines and execution-based evaluation
- Open challenges and hands-on lab overview

## Build

To rebuild the PDF from source (requires a LaTeX distribution with Beamer):

```bash
latexmk -pdf tutorial-preview.tex
```
