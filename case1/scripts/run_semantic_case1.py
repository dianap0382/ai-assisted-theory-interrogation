from pathlib import Path
import pandas as pd,numpy as np
from sentence_transformers import SentenceTransformer
r=Path(__file__).resolve().parents[1];d=pd.read_csv(r/'data/cvc_incentive_screen.csv').fillna('');anchors=['design compensation and performance incentives for corporate venture managers with bonuses equity or carried interest','corporate incentives to invest for access to innovation and strategic opportunities'];results=[]
for modelname in ['sentence-transformers/all-MiniLM-L6-v2','sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2']:
 m=SentenceTransformer(modelname);E=m.encode(anchors+d.context.astype(str).tolist(),normalize_embeddings=True,show_progress_bar=False);S=E[2:]@E[:2].T
 for i, row in enumerate(d.itertuples()):results.append(dict(model=modelname,source_row_id=row.source_row_id,file_name=row.file_name,cluster=row.cluster,compensation_similarity=float(S[i,0]),strategic_similarity=float(S[i,1]),compensation_preferred=bool(S[i,0]>S[i,1])))
pd.DataFrame(results).to_csv(r/'outputs/sentence_embedding_results.csv',index=False);print('Saved',len(results),'semantic rows')
