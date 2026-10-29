# Technical documentation

## Data and workflow

These five cases use case-specific subsets of prior corporate-venturing research material. Cases 1–3 use saved, extracted academic-source contexts rather than distributing complete journal PDFs; Cases 4–5 use segment-level numerical indicators without raw interview passages. Source and intermediate variables are retained where necessary for the case-specific computations.

## Lexical and semantic methods

TF–IDF (word unigrams/bigrams) and cosine similarity measure lexical proximity to text anchors. Optional multilingual and English sentence-transformer comparisons measure semantic proximity, without treating either score as definitive evidence of conceptual identity. Case-specific dictionaries and parameters are in the corresponding `config/` directories. Local scripts write outputs to their `outputs/` directories.

## Practice and tension measures

The underlying interview pipeline segmented minimally cleaned transcripts into overlapping windows of two sentences, after filtering sentences shorter than 30 characters. Matches to 13 practice dictionaries were counted; each segment's primary practice was the category with the largest match count (ties resolved in dictionary order). Unmatched segments were dropped. Lexical ostensive invocation was defined with a global 80th-percentile TF–IDF threshold. PIR indicates procedural, semantic or temporal markers; TI indicates simultaneous ostensive invocation and a deviation marker. These are screening indicators, not independently validated evidence of organizational transformation.

## Limitations

The repository verifies specified case-level operations, not the full upstream creation of the paper or interview corpora. Human interpretation remains necessary to adjudicate organizational mechanisms. The prior practice co-occurrence network is not reported as an empirical finding because its segment-key logic has not been independently validated. Independent source-PDF checking requires separately obtained authorized copies of the cited publications.
