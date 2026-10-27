# Corporate Venturing Research — public code candidate

**Review before publishing.** This is a conservative code-only subset of the five-case internal handoff. It is not a fully reproducible public dataset or a validated public release.

## Included
- `case1/scripts` — selected processing and similarity scripts for incentive comparisons.
- `case2/scripts` — scripts for autonomy analysis and internal consistency checks; some require missing restricted inputs.
- `case3/scripts` — selected partner/integration processing and similarity scripts.
- `case4/config/deviation_cues.json` and `case5/config/cue_dictionary.json` — general procedural/semantic/temporal regex dictionaries, corrected to match the Milestone 3 marker family.

## Deliberately excluded
Interview transcripts, extracted interviews and contexts, personal/source identifiers, source-audit CSVs, academic full-text extracts, all notebooks (which may contain inline research data), numeric indicators, analysis outputs, restricted records, provenance pointing to private archives, and exploratory co-occurrence analysis.

## Reproducibility limits
Scripts may require restricted datasets and configuration not included in this candidate. This archive intentionally does not claim end-to-end reproducibility. Full internal handoff and data provenance are maintained separately on access-controlled project storage.

## Exploratory co-occurrence
Milestone 4 Action 4 was exploratory and is not included because grouping on `segment_id` alone could mix distinct interviews. Treat co-occurrence analysis as unvalidated, not an empirical finding.

## Publication checklist
Before making this repository public, research supervisors should review the remaining scripts and category descriptions for disclosure risk and ensure that the proposed scope has project approval. Do not upload the accompanying restricted ZIP to public GitHub.
