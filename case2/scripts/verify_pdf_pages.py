"""Find original full pages in Everything.zip by filename, using text matching.
Copyright-sensitive raw PDFs and full-page transcriptions are NOT copied into the distributable package.
Returns page indices and short verification text only. Candidate scores need human checking.
"""
import argparse, difflib, io, re, zipfile
from pathlib import Path
import pandas as pd
import fitz
BASE=Path(__file__).resolve().parents[1]

def normalize(s):return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9 ]',' ',str(s).lower())).strip()
def main(zip_path):
 m=pd.read_csv(BASE/'data/academic_pdf_manifest.csv')
 src=pd.read_csv(BASE/'data/case2_cluster_source_rows.csv')
 lookup=m.drop_duplicates('filename').set_index('filename').zip_path.to_dict()
 out=[]
 with zipfile.ZipFile(zip_path) as z:
  cache={}
  for _,r in src.iterrows():
   name=r.source_pdf;path=lookup.get(name)
   if path is None:
    out.append({'side':r.side,'cluster':r.cluster_id,'source_row':r.source_row_index_zero_based,'source_pdf':name,'page':None,'match_score':0,'status':'PDF_NOT_FOUND'});continue
   if path not in cache:
    pdf=fitz.open(stream=z.read(path),filetype='pdf')
    cache[path]=[page.get_text(sort=True) for page in pdf]
    pdf.close()
   pages=cache[path]
   query=normalize(r.context)
   toks=[t for t in query.split() if len(t)>2]
   # Match overlap of context 4-grams; snippets frequently contain ellipses and extraction artifacts.
   grams={' '.join(toks[j:j+4]) for j in range(max(0,len(toks)-3)) if len(toks[j:j+4])==4}
   anchors=list(grams)
   scored=[]
   for i,p in enumerate(pages):
    q=normalize(p)
    coverage=sum(a in q for a in anchors)/max(1,len(anchors))
    scored.append((coverage,i))
   score,index=max(scored)
   excerpt=re.sub(r'\s+',' ',pages[index])[:240]
   out.append({'side':r.side,'cluster':int(r.cluster_id),'source_row':int(r.source_row_index_zero_based),'source_pdf':name,'page':index+1,'match_score':round(score,4),'status':'LOW_CONFIDENCE_MANUAL_SEARCH' if score<0.08 else 'CANDIDATE_VERIFY_MANUALLY','page_opening_for_manual_check':excerpt})
 pd.DataFrame(out).to_csv(BASE/'outputs/source_page_matching_to_review.csv',index=False)
 print('Checked',len(out),'rows, page suggestions saved. Human verification required.')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--source-zip',required=True);x=a.parse_args();main(x.source_zip)
