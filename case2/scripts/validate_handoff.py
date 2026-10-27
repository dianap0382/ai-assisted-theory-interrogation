from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
checks={}
manifest=pd.read_csv(ROOT/'outputs/corpus_manifest_recomputed.csv')
checks['163_distinct_pdf_hashes']=manifest['sha256'].nunique()==163
checks['30_source_rows']=len(pd.read_csv(ROOT/'data/case2_cluster_source_rows.csv'))==30
checks['264_kwic_rows']=len(pd.read_csv(ROOT/'data/case2_autonomy_kwic_original.csv'))==264
neighbors=pd.read_csv(ROOT/'outputs/tfidf_semantic_candidate_neighbors.csv')
checks['semantic_results_30_rows']=len(neighbors)==30 and neighbors['semantic_cosine_similarity'].notna().all()
checks['alternative_results_30_rows']=len(pd.read_csv(ROOT/'outputs/alternative_embedding_candidate_neighbors.csv'))==30
checks['page_candidates_30_rows']=len(pd.read_csv(ROOT/'outputs/case2_source_audit_30_rows.csv'))==30
checks['private_interview_text_absent']=not (ROOT/'data/interviews').exists()
print(json.dumps({key: bool(value) for key,value in checks.items()},indent=2))
if not all(checks.values()): raise SystemExit('Integrity check failed')
