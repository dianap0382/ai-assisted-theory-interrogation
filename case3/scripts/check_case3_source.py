"""Re-verify case-3 source page hashes against original Everything.zip archive.
Usage: python scripts/check_case3_source.py --archive /path/to/Everything.zip
"""
import argparse,zipfile,fitz,pandas as pd,hashlib
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--archive',required=True); args=ap.parse_args()
root=Path(__file__).resolve().parents[1]; tbl=pd.read_csv(root/'source_audit/practice_level_crosswalk.csv')
with zipfile.ZipFile(args.archive) as z:
 byfile={n:fitz.open(stream=z.read(n),filetype='pdf') for n in tbl.source_archive_path.unique()}
 for _,r in tbl.iterrows():
  tx=byfile[r.source_archive_path][int(r.pdf_page_1indexed)-1].get_text(sort=True)
  assert hashlib.sha256(tx.encode()).hexdigest()==r.source_text_sha256, r.evidence_id
print('OK: all source-page hashes match',len(tbl),'ledger rows')
