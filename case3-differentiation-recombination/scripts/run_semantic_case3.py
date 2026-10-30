"""Optional **actual sentence transformer** comparison. Run in an internet-enabled Python 3.11 environment.
Install: python -m pip install sentence-transformers pandas numpy scikit-learn
Execute from package root: python scripts/run_semantic_case3.py
The model is fetched from Hugging Face on first run, not packaged. Results are retrieval
sensitivity ONLY, NOT a rerun of the original CVC->OD clustering.
"""
from pathlib import Path
import csv, json, numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
root=Path(__file__).resolve().parents[1]
src=root/'source_audit'/'case3_source_page_contexts.csv'
with src.open(encoding='utf-8-sig',newline='') as f:
 rows=list(csv.DictReader(f))
print('Columns:', list(rows[0]) if rows else [])
# Select saved 400-character source snippets using schema found in the audit CSV, never silently fabricate content.
text_col=next((c for c in ['page_text','text','source_text','page_context','context','full_page_text','snippet_400chars'] if rows and c in rows[0]),None)
if text_col is None:
 raise ValueError('Source CSV does not contain passage text; no scores computed.')
rows=[r for r in rows if r.get(text_col,'').strip()]
if not rows: raise ValueError('No nonempty source passages to embed')
anchors={'integration_and_procurement':'startups run pilot projects with corporate business units and procurement managers decide to buy and onboard startups as suppliers','program_reorganization':'firms reorganize corporate venture capital and accelerator programs around startup supplier programs','cross_boundary_work':'joint project teams coordinate internal business units and external startup partners'}
models=['sentence-transformers/all-MiniLM-L6-v2','sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2']
out=[]
for model_id in models:
 model=SentenceTransformer(model_id)
 texts=[r[text_col] for r in rows]
 embeddings=model.encode(texts,normalize_embeddings=True,show_progress_bar=False)
 anchors_e=model.encode(list(anchors.values()),normalize_embeddings=True,show_progress_bar=False)
 scores=cosine_similarity(embeddings,anchors_e)
 for i,r in enumerate(rows):
  for j,k in enumerate(anchors):
   out.append({'model':model_id,'row_index':i,'source_page':r.get('pdf_page_1indexed',r.get('page','')),'anchor':k,'cosine_similarity':float(scores[i,j])})
p=root/'outputs'/'sentence_embedding_results.csv'
with p.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print('Saved',p,'rows',len(out))
