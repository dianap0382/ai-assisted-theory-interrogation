"""Reconcile research source archive; no silent change to the original published figure."""
import argparse,hashlib,json,zipfile
from pathlib import Path
import pandas as pd
BASE=Path(__file__).resolve().parents[1]
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source-zip',required=True);a=p.parse_args()
 with zipfile.ZipFile(a.source_zip) as z:
  names=[x for x in z.namelist() if x.lower().endswith('.pdf') and not x.startswith('__MACOSX')]
  records=[]
  for n in names:
   b=z.read(n); records.append({'zip_path':n,'filename':Path(n).name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
  df=pd.DataFrame(records);df['copies_with_same_sha256']=df.groupby('sha256')['sha256'].transform('size')
  df.to_csv(BASE/'outputs/corpus_manifest_recomputed.csv',index=False)
  result={'pdf_entries':len(df),'sha256_unique':df.sha256.nunique(),'duplicate_entries':len(df)-df.sha256.nunique(),'note':'Historical 172 figure not silently updated. Check original inclusion and filtering definitions.'}
  (BASE/'outputs/corpus_reconciliation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
