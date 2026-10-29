# AI-Assisted Theory Development

Companion repository to the research proposal *AI-Assisted Theory Development: Interrogating Theory Through Its Computational Representation*. It contains five case-level computational analyses demonstrating the proposed approach.

**Where to start:** to run the analyses, go to [Getting started](#getting-started). To understand the approach, read the [Overview](#overview) and the [Analytical framework](#analytical-framework). To check results case by case, see [The five cases](#the-five-cases).

## Overview

Theory makes complex empirical phenomena intelligible by specifying constructs, the distinctions and relationships among them, and the mechanisms that account for those phenomena. This specification also shapes what researchers can see.

To search large bodies of text, theory must first be encoded in a computational representation: dictionaries, embeddings, similarity measures, and mapping rules. Applied at scale, this representation recognizes what resembles existing constructs and systematically overlooks what does not. When used only to classify evidence into existing constructs, computational methods reproduce existing theory more efficiently.

We develop an architecture in which **theory both structures the search and is what the search examines**. The computational representation detects where theory holds or breaks down; human adjudication distinguishes computational artifacts from theoretical opportunities. AI does not develop theory. It expands systematic, human-directed search for theoretical opportunities, while explanation and inference remain with researchers.

The repository demonstrates the architecture through five candidate cases in corporate venturing, drawing on organizational design theory, corporate venturing scholarship, and practitioner interviews.

## What this repository supports

**The repository supports:**

- Reproduction of specified case-level computational analyses.
- Verification of selected indicators.
- Inspection of available supporting analytical records.

**It does not support:**

- Reconstruction of the original literature and interview corpora.
- Independent reproduction of researcher adjudication or theoretical interpretations.

See [Reproducibility and verification](#reproducibility-and-verification) for what each kind of check establishes.

## Repository layout

```text
.
├── README.md
├── TECHNICAL_DOCUMENTATION.md   # computational descriptions and decisions
├── requirements.txt
└── case1/ … case5/
    ├── scripts/                 # run_* and verify_* scripts
    └── outputs/                 # saved results and supporting records
```

> [DIANA: Confirm where each case stores its input data and whether the layout above is complete.]

## Getting started

Use **Python 3.11 or later** (core scripts checked with Python 3.13.5). Create a virtual environment, activate it using the command appropriate to your operating system, and install the dependencies listed in [`requirements.txt`](requirements.txt).

From the repository root, execute the following commands. The scripts access their inputs and save generated results within their respective case directories.

> [DIANA: Also confirm whether running the scripts overwrites saved reference outputs. If so, specify how reviewers should preserve the originals or perform comparisons against the committed versions.]

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt

# Core case-level analyses
python case1/scripts/run_case1.py
python case2/scripts/run_case2.py
python case3/scripts/run_case3.py
python case4/scripts/verify_case4.py
python case5/scripts/verify_case5.py

# Optional semantic embedding analyses
python case1/scripts/run_semantic_case1.py
python case3/scripts/run_semantic_case3.py
```

> [DIANA: Please confirm that all five core scripts and both optional semantic scripts execute correctly when invoked from the repository root, exactly as shown in the README.]

The core lexical analyses and indicator checks do not require pretrained models. The optional semantic analyses download the specified sentence-transformer models on first use.

Generated results are saved in each case’s `outputs/` directory. The case-specific instructions in [The five cases](#the-five-cases) identify which results can be reproduced and how to compare them with the saved outputs.

## Analytical framework

### Four epistemic questions

The architecture is organized around four epistemic functions. Each function poses one question to theory:

1. **Recognition:** Does theory see the phenomenon?
2. **Differentiation:** Do its distinctions hold?
3. **Dynamics:** What happens to practices in enactment?
4. **Limits:** What remains persistently unexplained?

### From signal to theoretical elaboration

A signal is not a finding. The six-step cycle proceeds under human adjudication:

1. **Detect:** The computational representation detects a signal.
2. **Return to evidence:** Researchers examine the passages or interview segments that produced the signal.
3. **Representational sensitivity:** Researchers test whether the signal persists when dictionaries, models, or granularity are altered.
4. **Puzzle:** A surviving signal is stated as a theoretical puzzle using the question its epistemic function poses.
5. **Rival explanations:** Researchers assess whether existing theory already accounts for the pattern, whether it is a contextual variation of a known mechanism, or whether it points to something theory omits.
6. **Elaboration:** If rival explanations do not account for the pattern, researchers determine whether to redraw a construct boundary, specify a configuration of mechanisms, add a contingency or process of change, or state the limits of theory’s scope.

Returning to the evidence can itself dissolve a signal. The cycle is designed to record the signal, evidence, checks, rival explanations considered, and decision taken, making human adjudication auditable rather than tacit. Theoretical elaboration can then revise the computational representation so that the search begins again.

### Comparisons and indicators

The five cases draw on two complementary comparisons.

**Comparison A**: Corporate venturing scholarship and organizational design theory. Practices identified in corporate venturing research are mapped against organizational design constructs. Mapping patterns generate candidate signals of preservation, decomposition, recombination, and non-fit, allowing researchers to examine whether existing theoretical constructs recognize and adequately differentiate the practices described in the literature.

**Comparison B**: Practitioner enactment and ostensive baselines. Interview evidence is compared with literature-derived descriptions of organizational practices. Three diagnostic measures characterize the relationship between established expectations and reported enactment. The Ostensive Invocation Rate has two variants: OIR-L measures lexical invocation of the literature-derived baseline, while OIR-S measures semantic invocation. The Performative Improvisation Rate (PIR) measures departures from that baseline. The Tension Index (TI) identifies instances in which practitioners invoke the baseline's vocabulary while describing departures from it. These indicators inform the practitioner-based analyses in Cases 4 and 5; they do not independently establish theoretical mechanisms or whether a reported practice was actually enacted.

These comparisons produce signals for the four epistemic functions. The six-step theory interrogation cycle then determines whether a signal reflects a computational artifact, an observation already explained by existing theory, or an opportunity for theoretical elaboration.

> [DIANA: For Cases 4 and 5, specify which of OIR-L, OIR-S, PIR, and TI appear in the saved outputs, and confirm that `TECHNICAL_DOCUMENTATION.md` explicitly links each to the case-level diagnostic signal and the subsequent qualitative adjudication.]

## The five cases

The five cases illustrate how computational representations can support the four epistemic functions of theory interrogation. Each case provides a reproducible computational comparison or verification check that supports the theory interrogation process, and each analysis generates or examines diagnostic signals that require interpretation against the underlying evidence. Reviewers can execute the scripts listed below and compare their results with the saved outputs.

**Suggested reading order**: Begin with [Case 4](#case-4-early-stage-investment--dynamics-tension) for the full theory interrogation cycle, then examine Cases 1, 2, 3, and 5 to see how different diagnostic signals are qualified, remain provisional, or dissolve under further examination.

| Case | Topic | Epistemic function (signal) | Script | Mode |
|------|-------|-----------------------------|--------|------|
| 1 | Incentives | Recognition (preservation) | [`run_case1.py`](case1/scripts/run_case1.py); optional [`run_semantic_case1.py`](case1/scripts/run_semantic_case1.py) | Regenerates results |
| 2 | Autonomy | Differentiation (decomposition) | [`run_case2.py`](case2/scripts/run_case2.py) | Regenerates results |
| 3 | Partner integration | Differentiation (recombination) | [`run_case3.py`](case3/scripts/run_case3.py); optional [`run_semantic_case3.py`](case3/scripts/run_semantic_case3.py) | Regenerates results |
| 4 | Early-stage investment | Dynamics (tension) | [`verify_case4.py`](case4/scripts/verify_case4.py) | Verifies saved indicators |
| 5 | Fast-track governance | Limits (candidate non-fit) | [`verify_case5.py`](case5/scripts/verify_case5.py) | Verifies saved indicators |

### Case 1: Incentives | Recognition (preservation)

**Examines:** whether incentive-related practices in corporate venturing are recognized by existing organizational design constructs.

**Run:** [`case1/scripts/run_case1.py`](case1/scripts/run_case1.py) for TF-IDF comparisons of theoretical anchors and literature-derived passages; it regenerates [`case1/outputs/tfidf_similarity.csv`](case1/outputs/tfidf_similarity.csv). Optionally run [`case1/scripts/run_semantic_case1.py`](case1/scripts/run_semantic_case1.py) for sentence-embedding comparisons; it regenerates [`case1/outputs/sentence_embedding_results.csv`](case1/outputs/sentence_embedding_results.csv).

**Verify:** Compare the regenerated files with the saved results.

> [DIANA: Confirm these are the correct generated output files. Specify whether exact matches or numerical tolerances are expected, including any differences between TF-IDF and sentence-embedding results.]

**Not reproduced:** Other saved outputs, including `cvc_od_candidate_crosswalk.csv`, `dictionary_sensitivity.csv`, and `qualification_report.json`, document supporting analyses and qualification decisions that these scripts do not regenerate.

> [DIANA: Confirm which additional saved outputs are not regenerated and whether any are independently verifiable.]

**Outcome:** The computational comparisons inform the recognition assessment, but the evidence does not yet establish a qualified preservation finding.

### Case 2: Autonomy | Differentiation (decomposition)

**Examines:** whether established theoretical categories adequately distinguish dimensions of corporate venturing unit autonomy.

**Run:** [`case2/scripts/run_case2.py`](case2/scripts/run_case2.py) to reproduce the candidate-row provenance checks, dictionary-sensitivity analysis, and lexical comparisons.

**Verify:** Compare the generated results with the corresponding saved outputs.

> [DIANA: Identify the exact output filenames generated by this script, the saved files reviewers should compare, and the expected matching criteria or numerical tolerances. Confirm whether any checks report explicit pass/fail results.]

**Not reproduced:** The original full-corpus clustering.

**Outcome:** The decomposition signal remains sensitive to representational choices and does not independently establish a stable theoretical distinction.

### Case 3: Partner integration | Differentiation (recombination)

**Examines:** whether empirical practices suggest connections between theoretical constructs that are ordinarily treated separately.

**Run:** [`case3/scripts/run_case3.py`](case3/scripts/run_case3.py) for dictionary screening and candidate similarity analysis. Optionally run [`case3/scripts/run_semantic_case3.py`](case3/scripts/run_semantic_case3.py) for sentence-embedding comparisons.

**Verify:** Compare the generated screening and similarity results with the corresponding saved outputs.

> [DIANA: Identify the exact output filenames generated by each script, which saved files should be compared, and whether exact agreement or specified numerical tolerances are expected. Distinguish regenerated results from supporting analytical outputs.]

**Outcome:** The computational results inform a descriptive recombination assessment. Recombination is supported descriptively within one article, but independent recurrence has not been established.

### Case 4: Early-stage investment | Dynamics (tension)

**Examines:** why a corporate venturing unit with formal authority over its investment-stage strategy nevertheless abandons early-stage investing. This case illustrates the full six-step theory interrogation cycle.

**Run:** [`case4/scripts/verify_case4.py`](case4/scripts/verify_case4.py) to check the saved pseudonymized indicator tables and case-level distinctions.

**Verify:** Examine the script’s reported checks against the saved indicators.

> [DIANA: Identify the exact input and output files involved, the indicators and distinctions checked, and the expected results or pass/fail criteria. Clarify whether the script regenerates any outputs or only verifies existing data.]

**Not reproduced:** These checks support the computational component of the tension assessment. They do not independently reproduce the underlying interview interpretation or the theoretical elaboration concerning formal decision authority and buffering from the parent firm’s expectation horizon.

**Outcome:** The resulting theoretical elaboration distinguishes formal decision authority from the organizational buffering required to sustain an early-stage investment strategy when the parent firm’s expectation horizon is misaligned with the investment stage.

### Case 5: Fast-track governance | Limits (candidate non-fit)

**Examines:** whether an apparent mismatch between established theory and empirical practice indicates a theoretical limit.

**Run:** [`case5/scripts/verify_case5.py`](case5/scripts/verify_case5.py) to check the saved indicator data and threshold sensitivity.

**Verify:** Examine the reported indicator and sensitivity checks against the saved results.

> [DIANA: Identify the exact input and output files involved, the thresholds examined, and the expected results or pass/fail criteria. Clarify whether the script regenerates any outputs or only verifies existing data.]

**Not reproduced:** The computational checks do not independently establish whether the fast-track procedure was enacted.

**Outcome:** Returning to the evidence shows that the fast-track procedure was proposed rather than enacted, so the candidate non-fit does not survive qualitative adjudication.

## Reproducibility and verification

### What verification means

Successful computational reproduction establishes consistency of the reported indicators and comparisons. It does not, by itself, establish the validity of a theoretical interpretation, and it does not independently validate or reproduce researcher adjudication.

For each case, successful verification means that regenerated outputs agree with saved results according to documented comparison criteria, or that verification scripts confirm the specified indicators and analytical checks.

> [DIANA: Confirm the applicable numerical tolerances, any requirements for model versions or random seeds, and whether successful execution alone is sufficient for Cases 4 and 5 or specific assertions must pass. The sentence above holds only if the verification scripts actually implement these checks.]

### Three categories of evidence

The repository distinguishes three categories of evidence:

1. **Regenerated computational results:** Outputs produced by the supplied scripts that reviewers can compare with saved results.
2. **Verified indicators:** Existing data and analytical distinctions checked by verification scripts against specified criteria.
3. **Supporting analytical records:** Additional outputs, source-level assessments, and researcher adjudication that are documented but not independently regenerated.

Some files in each case’s `outputs/` directory belong to this third category: they document supporting analyses and researcher adjudication rather than outputs regenerated by the listed scripts.

### What is and is not included

The repository contains the data needed for the listed case-specific scripts. It does not reconstruct all source PDFs, original interview text, full-corpus clustering, or researcher adjudication decisions. Cases 4 and 5 contain pseudonymized numerical segment indicators rather than original interview quotations. Research context snippets in Cases 1–3 derive from published academic sources; attribution and reuse rights remain governed by the underlying publications. The analyses are diagnostic screens, not proof of causal mechanisms or a substitute for qualitative validation.

## Further documentation, citation, and license

Detailed computational descriptions and decisions are summarized in [`TECHNICAL_DOCUMENTATION.md`](TECHNICAL_DOCUMENTATION.md), which records the available analytical procedures, evidence, and researcher adjudication, and identifies limitations in what can be independently reproduced.

**Citation:** [TODO: add once the journal’s anonymous review requirements allow. A `CITATION.cff` file names authors, so add it only when that is permitted.]

**License:** [TODO: decide after clarifying which components (code, text snippets from published sources, pseudonymized interview indicators) may be shared and under what terms. A standard software license may not cover the underlying published or interview-derived materials.]
