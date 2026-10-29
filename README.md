# Corporate venturing routine analysis

This repository contains five reproducible case-specific analyses developed for a research proposal on corporate venturing routines and organizational design. The cases provide examples of how literature-derived constructs can be compared, qualified, or challenged by empirical passages and quantitative indicators. They are case-level demonstrations, not a regeneration of the original full literature or interview corpora.

## Getting started

Use **Python 3.11 or later** (core scripts checked with Python 3.13.5). Create an environment and install `requirements.txt`. From the repository root, run the scripts below. All paths are relative to each case folder. The lexical and indicator checks run without pretrained models; semantic scripts require downloading the specified sentence-transformer models on first use. Outputs are saved under each case's `outputs/` directory.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python case1/scripts/run_case1.py
python case2/scripts/run_case2.py
python case3/scripts/run_case3.py
python case4/scripts/verify_case4.py
python case5/scripts/verify_case5.py
```

## Case guide

- **Case 1: Incentives.** Run `case1/scripts/run_case1.py` to compare incentive and strategic-value anchors with saved literature context rows using TF–IDF; optionally run `run_semantic_case1.py` for sentence embedding comparison.
- **Case 2: Autonomy.** Run `case2/scripts/run_case2.py` for candidate-row provenance checks, dictionary-sensitivity and lexical comparison. The full original paper-corpus clustering is outside this case-specific run.
- **Case 3: Partner integration.** Run `case3/scripts/run_case3.py` for dictionary screening and candidate similarity; optionally run `run_semantic_case3.py` for embedding comparisons.
- **Case 4: Early-stage investment.** Run `case4/scripts/verify_case4.py` to check the saved, pseudonymized indicator tables and case-level distinctions.
- **Case 5: Fast-track governance.** Run `case5/scripts/verify_case5.py` to check the saved indicator data and threshold sensitivity.

## Reproducibility scope

The repository contains the data needed for the listed case-specific scripts. It does not reconstruct all source PDFs, original interview text, full-corpus clustering, or researcher adjudication decisions. Case 4 and 5 contain pseudonymized numeric segment indicators, not original quotations. Research context snippets in Cases 1–3 derive from published academic sources; attribution and reuse rights remain governed by the underlying publications. The analyses are diagnostic screens, not proof of causal mechanisms or a substitute for qualitative validation.

Detailed computational descriptions and decisions are summarized in `TECHNICAL_DOCUMENTATION.md`.
