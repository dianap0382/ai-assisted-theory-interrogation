from pathlib import Path
import json,re,numpy as np,pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
r=Path(__file__).resolve().parents[1];d=pd.read_csv(r/'data/cvc_incentive_screen.csv').fillna('');cfg=json.loads((r/'config/case1.json').read_text());anchors=cfg['anchors'];v=TfidfVectorizer(stop_words='english',ngram_range=(1,2));X=v.fit_transform(list(anchors.values())+d.context.astype(str).tolist());s=cosine_similarity(X[2:],X[:2]);t=d[['source_row_id','file_name','cluster','keyword','context']].copy();t['tfidf_compensation']=s[:,0];t['tfidf_strategic']=s[:,1];t['compensation_more_similar']=s[:,0]>s[:,1];t.to_csv(r/'outputs/tfidf_similarity.csv',index=False);print('TF-IDF computed for',len(d),'rows; independent practice-level validation still required.')
