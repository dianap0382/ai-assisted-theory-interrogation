import nbformat as nbf
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
n=nbf.v4.new_notebook()
c=[]
def md(x):c.append(nbf.v4.new_markdown_cell(x))
def code(x):c.append(nbf.v4.new_code_cell(x))
md('''# Case 2 — Autonomy of corporate venture capital units

**Comparison (a) · candidate decomposition · reproducibility test**

The purpose is to show how a proposed decomposition signal can be traced to saved clustering rows and original sources, then challenged under alternate representations. This notebook deliberately excludes researcher names, private transcripts, generative modeling, and unsupported claims of robustness. **Steps 4–6 are reserved for subsequent theoretical adjudication.**

**Important:** This is the *testing* notebook. Some case-level checks have executed; global 163-document regeneration and semantic-model sensitivity must still be run in a fully provisioned local environment. The saved cluster identifiers are historical outputs, not reproducible from the 30 case-selected records alone.
''')
code('''from pathlib import Path
import pandas as pd, json, sys
from IPython.display import display
BASE = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
sys.path.insert(0, str(BASE/'scripts'))
from run_case2 import do_run
report = do_run(semantic=False)
display(pd.DataFrame([report]))''')
md('''## Step 1 — Detect

Original preselected CVC clusters: **347, 564, 580, 673**. Original OD clusters: **18, 82, 92, 116**. Display original row counts, unique document hashes, and source-row keys. These are **candidate** connections, not verified one-to-one mappings. The source-table labeling fields on the CVC side were empty in the archive; we do not fabricate them.
''')
code('''display(pd.read_csv(BASE/'outputs/cluster_provenance.csv'))
display(pd.read_csv(BASE/'data/autonomy_OD_cluster_candidates.csv')[['cluster','Category 1','Category 2','Category 3']])''')
md('''**Qualification / proposed Step 1 outcome:** candidate decomposition, subject to human source inspection and Step 3 perturbations. The original cluster and correspondence computation is in the supplied historical notebooks; rerunning the source corpus would be necessary to assert exact reproduction.
''')
md('''## Step 2 — Return to the evidence

Consult `data/case2_cluster_source_rows.csv` for exact row keys and source filenames; consult the separate page-matching file when generated from `Everything.zip`. Page candidates are **not confirmed quotations**. Examine full, original PDF paragraphs and record manually verified page and interpretation. Published author names and bibliographic titles are appropriate source metadata; personal researcher names are omitted.

Verified high-value primary source: Hill et al. (2009), print p. 8, distinguishes vertical discretion against the corporate hierarchy from horizontal discretion against business units, and print p. 13 operationalizes investment/exit decisions and business-unit approvals. Frey & Kanbach (2024) pp. 2804–2805 discuss parent control and discretionary rights. Fels et al. (2021) pp. 80–82 contrast levels and purposes of autonomy. **Only cite passages after checking against the original page, not the KWIC truncation.**
''')
code('''evidence=pd.read_csv(BASE/'data/case2_cluster_source_rows.csv')
display(evidence[['side','cluster_id','source_row_index_zero_based','source_pdf','practice_text']].head(30))
p=BASE/'outputs/source_page_matching_to_review.csv'
if p.exists(): display(pd.read_csv(p)[['side','cluster','source_pdf','page','match_score','status']])
else: print('To compute all source-page candidates: python scripts/verify_pdf_pages.py --source-zip /path/to/Everything.zip')''')
md('''**Proposed Step 2 outcome:** the recovered articles support the *existence* of several autonomy dimensions, but a claim about *algorithmic decomposition* requires verified mapping and source recurrence across the full dataset. Do not assert that all cited passages belong to every candidate cluster.
''')
md('''## Step 3 — Representational sensitivity

**3A: Split dictionary.** Explicit vertical, horizontal, and investment-decision keywords are checked against all 264 saved KWIC rows. Counts are overlapping, depend on abbreviated context, and are not independent article counts.

**3B: TF-IDF lexical neighbors.** Computed from the exact same 30 case-selected source rows, identifying whether nearest lexical contexts retain the original local saved cluster. This is *not* the original global DBSCAN clustering.

**3C: Sentence embedding original / alternate.** Run `python scripts/run_case2.py --semantic` after installing requirements and model downloads. Compare neighbor assignments on the same 30 rows. A separate global-corpus embedding and clustering rerun is required for full original cluster stability claims.
''')
code('''display(pd.read_csv(BASE/'outputs/kwic_sensitivity_summary.csv'))
display(pd.read_csv(BASE/'outputs/tfidf_candidate_row_neighbors.csv')[['row_key','lexical_nearest_row_key','lexical_cosine_similarity','lexical_nearest_same_saved_cluster']])
for name in ['tfidf_semantic_candidate_neighbors.csv','alternative_embedding_candidate_neighbors.csv']:
 path=BASE/'outputs'/name
 if path.exists():display(pd.read_csv(path))
 else: print(name,'NOT RUN — requires sentence-transformers and downloaded model weights')''')
md('''## Case record (Steps 1–3 only)

1. **Detect:** candidate decomposition; original cluster identities and evidence rows recorded; qualification as a substantive theoretical signal remains provisional.
2. **Evidence:** full sources available; source and page suggestions traceable; context and cluster mappings require manual adjudication.
3. **Sensitivity:** dictionary and candidate TF-IDF test executed; semantic test and full 163-PDF analysis are pending external dependency downloads and full pipeline checks.

**Decision at this stage:** *provisional / not submission-certified*. Keep the adjudication record open; the outcome may persist, disappear, or change under full sensitivity analyses. No interview materials enter this case.
''')
n['cells']=c;n['metadata']={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}}
nbf.write(n,ROOT/'notebooks/case2_autonomy.ipynb')
print('Wrote notebook',len(c),'cells')
