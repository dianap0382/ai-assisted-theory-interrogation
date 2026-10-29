"""Case 2 reproducibility TEST runner. No generative models.
Outputs are derived from saved candidate rows, with honest scope labels.
This does not silently substitute case-level reclustering for original 163-paper corpus clustering.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, re, sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import yaml

BASE=Path(__file__).resolve().parents[1]
D=BASE/'data'; O=BASE/'outputs'; CFG=BASE/'config'/'case2.yml'

def do_run(semantic=False):
 O.mkdir(exist_ok=True)
 cfg=yaml.safe_load(CFG.read_text(encoding='utf-8'))
 src=pd.read_csv(D/'case2_cluster_source_rows.csv').copy()
 src['row_key']=src.apply(lambda r:f"{r['side']}:{int(r['cluster_id'])}:{int(r['source_row_index_zero_based'])}",axis=1)
 assert len(src)==30 and not src.row_key.duplicated().any(), 'Source audit rows unexpectedly changed'
 src['context']=src['context'].fillna('').astype(str)
 src['practice_text']=src['practice_text'].fillna('').astype(str)
 src['text_for_test']=(src['context']+' '+src['practice_text']).str.strip()
 src['source_hash']=src['sha256'].fillna('').astype(str)
 src['source_identity']=src['source_hash'].where(src['source_hash'].str.len()>0,src['source_pdf'])
 rows=[]
 for side,g in src.groupby('side'):
  for cid,h in g.groupby('cluster_id'):
   rows.append({'comparison':side,'cluster':int(cid),'original_candidate_rows':len(h), 'unique_pdf_contents_within_cluster':h.source_identity.nunique(), 'source_row_keys':'; '.join(h.row_key)})
 pd.DataFrame(rows).sort_values(['comparison','cluster']).to_csv(O/'cluster_provenance.csv',index=False)
 kwic=pd.read_csv(D/'case2_autonomy_kwic_original.csv');kwic['context']=kwic.context.fillna('').astype(str)
 labels=cfg['sensitivity']['dictionary']
 for col,phrases in labels.items():
  pat='|'.join(re.escape(p) for p in phrases)
  kwic[col]=kwic.context.str.contains(pat,case=False,regex=True)
 kwic.insert(0,'kwic_row_index_zero_based',np.arange(len(kwic)))
 kwic.to_csv(O/'kwic_split_dictionary_flags.csv',index=False)
 stats={'total_original_kwic_rows':len(kwic),'unique_exact_kwic_rows':int(len(kwic.drop_duplicates(subset=['file_name','category','keyword','context','practices']))), 'unique_source_filenames':int(kwic.file_name.nunique())}
 for k in labels: stats[f'{k}_hits']=int(kwic[k].sum())
 pd.DataFrame([stats]).to_csv(O/'kwic_sensitivity_summary.csv',index=False)
 # Lexical representation over EXACT SAME candidate row text units; a local sensitivity test, not full-corpus reproduction.
 text=src.text_for_test.tolist()
 vec=TfidfVectorizer(stop_words='english',ngram_range=(1,2),min_df=1,max_features=cfg['sensitivity']['tfidf_max_features'])
 x=vec.fit_transform(text)
 lex_sim=cosine_similarity(x)
 saved_ids=src.cluster_id.astype(int).to_numpy()
 output=src[['row_key','side','cluster_id','source_pdf']].copy()
 # Rankings are more interpretable than 30-row DBSCAN, which cannot recreate the saved global cluster IDs.
 ix=np.argsort(-lex_sim,axis=1)
 for i in range(len(output)):
  alt=next((int(j) for j in ix[i] if int(j)!=i),None)
  output.loc[i,'lexical_nearest_row_key']=src.iloc[alt].row_key
  output.loc[i,'lexical_cosine_similarity']=round(float(lex_sim[i,alt]),6)
  output.loc[i,'lexical_nearest_same_saved_cluster']=bool(src.iloc[alt].side==src.iloc[i].side and saved_ids[alt]==saved_ids[i])
 output.to_csv(O/'tfidf_candidate_row_neighbors.csv',index=False)
 report={'stage':'non_neural_test_completed','n_candidate_rows':len(src),'n_kwic':len(kwic),'saved_cvc_clusters':cfg['cvc_clusters'],'saved_od_clusters':cfg['od_clusters'], 'same_cluster_nearest_tfidf_fraction':round(float(output.lexical_nearest_same_saved_cluster.mean()),4), 'tfidf_scope':'30 saved case-2 candidate rows, not a rerun on the original 163-paper corpus','model_check':'not_executed'}
 if semantic:
  from sentence_transformers import SentenceTransformer
  import sklearn
  mdl=SentenceTransformer(cfg['original_model'])
  emb=mdl.encode(text,normalize_embeddings=True,show_progress_bar=False)
  sim=cosine_similarity(emb)
  neighbors=np.argsort(-sim,axis=1)
  for i in range(len(output)):
   alt=next((int(j) for j in neighbors[i] if int(j)!=i),None)
   output.loc[i,'semantic_nearest_row_key']=src.iloc[alt].row_key
   output.loc[i,'semantic_cosine_similarity']=round(float(sim[i,alt]),6)
   output.loc[i,'semantic_nearest_same_saved_cluster']=bool(src.iloc[alt].side==src.iloc[i].side and saved_ids[alt]==saved_ids[i])
  output.to_csv(O/'tfidf_semantic_candidate_neighbors.csv',index=False)
  report['model_check']='executed_original_model_on_30_candidate_contexts'
  report['sentence_transformers_scope']='local candidate-row sensitivity only; not full corpus clustering reproduction'
  # Alternative dictionary robustness is already computed on all saved KWIC rows.
  alt=SentenceTransformer(cfg['sensitivity']['alternative_embedder'])
  sim2=cosine_similarity(alt.encode(text,normalize_embeddings=True,show_progress_bar=False))
  results=[]
  for i in range(len(text)):
   j=int(next(j for j in np.argsort(-sim2[i]) if j!=i))
   results.append({'row_key':src.iloc[i].row_key,'alternative_model_neighbor':src.iloc[j].row_key,'alternative_model_cosine_similarity':round(float(sim2[i,j]),6)})
  pd.DataFrame(results).to_csv(O/'alternative_embedding_candidate_neighbors.csv',index=False)
  report['alternative_model_check']='executed_on_30_candidate_contexts'
 import sklearn
 report['software']={'python':platform.python_version(),'pandas':pd.__version__,'numpy':np.__version__,'scikit_learn':sklearn.__version__}
 (O/'test_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(json.dumps(report,indent=2))
 return report

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--semantic',action='store_true',help='Run downloaded pretrained embedding models on candidate contexts');arg=ap.parse_args()
 do_run(arg.semantic)
