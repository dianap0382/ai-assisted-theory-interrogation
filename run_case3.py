from pathlib import Path
import pandas as pd,numpy as np,json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
root=Path(__file__).resolve().parents[1]
a=pd.read_csv(root/'data/cvc_context_screened_rows.csv').fillna('')
config=json.loads((root/'config/case3.json').read_text())
rows=[]
for name,regex in config['dictionary_patterns'].items():
 flags=a.context.astype(str).str.contains(regex,case=False,regex=True)
 rows.append(dict(representation=name,total_screened=len(a),matched_rows=int(flags.sum()),n_sources=int(a.loc[flags,'file_name'].nunique()),n_clusters=int(a.loc[flags,'cluster'].nunique()),qualifies_recombination='not established'))
pd.DataFrame(rows).to_csv(root/'outputs/dictionary_sensitivity.csv',index=False)
anchors=config['anchors']; text=a.context.astype(str).tolist()
vec=TfidfVectorizer(stop_words='english',ngram_range=(1,2)); X=vec.fit_transform(list(anchors.values())+text)
sim=cosine_similarity(X[len(anchors):],X[:len(anchors)])
r=a[['file_name','cluster','keyword','context']].copy();r.insert(0,'source_row_id_screened',np.arange(len(a)))
for j,name in enumerate(anchors):r['tfidf_'+name]=sim[:,j]
r['best_anchor']=np.array(list(anchors))[sim.argmax(axis=1)];r['max_tfidf']=sim.max(axis=1)
r.sort_values('max_tfidf',ascending=False).to_csv(root/'outputs/tfidf_passage_neighbors.csv',index=False)
p=pd.read_csv(root/'source_audit/case3_source_page_contexts.csv').fillna('');p.insert(0,'page_hit_row_id',np.arange(len(p)))
for w in [120,240,400]:p[f'narrow_kw_window_{w}']=p.snippet_400chars.astype(str).str.slice(0,w).str.contains(config['dictionary_patterns']['narrow'],case=False,regex=True)
p.to_csv(root/'outputs/context_window_screen.csv',index=False)
print('Reproduced dictionary, TF-IDF and saved-window screening; NO embedding rerun.')
