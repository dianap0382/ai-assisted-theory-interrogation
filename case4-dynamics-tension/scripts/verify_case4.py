from pathlib import Path
import pandas as pd,json
r=Path(__file__).resolve().parents[1]
d=pd.read_csv(r/'data/p8_indicators_anonymized.csv')
s=pd.read_csv(r/'data/case4_selected_indicators.csv')
q=d[d['OIR_lexical'] & d['OIR_semantic'] & d['PIR'] & d['temporal_signal']]
ids={(a,b) for a,b in zip(q['interview_id'],q['segment_id'])}
expected={('unit_052',480),('unit_086',558),('unit_072',145),('unit_040',15)}
assert len(d)==490,(len(d),'unexpected P8 total')
assert len(q)==4 and ids==expected,ids
assert int(d['TI_lexical'].sum())==6
x=s.set_index(['interview_id','segment_id'])
assert bool(x.loc[('unit_086',8),'OIR_lexical']) and not bool(x.loc[('unit_086',8),'OIR_semantic'])
assert bool(x.loc[('unit_086',558),'OIR_semantic'])
assert bool(x.loc[('unit_040',15),'OIR_semantic'])
print('PASS: 490 P8 rows, 4 four-indicator temporal matches, 6 TI-L flags; 4b distinction verified.')
