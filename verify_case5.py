from pathlib import Path
import pandas as pd,json
root=Path(__file__).resolve().parents[1]
f=pd.read_csv(root/'data/case5_focal_numeric.csv');p7=pd.read_csv(root/'data/p7_screening_numeric.csv')
a=f.iloc[0];s=json.loads((root/'outputs/screening_summary.json').read_text())
assert len(f)==1 and len(p7)==70
assert a.interview_id=='participant_61652' and a.segment_id==509
assert not bool(a.OIR_lexical) and not bool(a.OIR_semantic) and bool(a.PIR) and not bool(a.TI_lexical)
assert bool(a.procedural_signal) and not bool(a.temporal_signal) and not bool(a.semantic_signal)
assert abs(float(a.tfidf_similarity)-s['focal']['tfidf_similarity'])<1e-10
assert abs(float(a.embedding_similarity)-s['focal']['embedding_similarity'])<1e-10
for k,n in s['p7_flag_totals'].items(): assert int(p7[k].sum())==n
v=pd.read_csv(root/'outputs/threshold_sensitivity.csv')
assert len(v)==4
for row in v.itertuples():
 assert bool(row.focal_lexical_pass)==bool(a.tfidf_similarity>=row.lexical_cutoff)
 assert bool(row.focal_semantic_pass)==bool(a.embedding_similarity>=row.semantic_cutoff)
print('PASS: Case 5 saved indicators, P7 totals and four cutoff sensitivity checks')
