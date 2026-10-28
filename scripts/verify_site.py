#!/usr/bin/env python3
"""Data integrity checks; remote availability and browser behavior are separate gates."""
from __future__ import annotations
import csv,json,re
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=('id','title','year','venue','direction','type','tags','problem','idea','contribution','evidence','statistics','potential','url','authors','scholars','arxiv','publication_status','publication_source','verification')
DIRECTIONS={'RLHF & Preference Alignment','Machine Unlearning','Watermark & AI Text Detection'}
TYPES={'Method','Theory','Theory + Method'}
def verify():
 html=(ROOT/'public/index.html').read_text()
 papers=json.loads((ROOT/'public/data/papers.json').read_text())
 scholars=json.loads((ROOT/'public/data/scholars.json').read_text())
 archive=json.loads((ROOT/'public/data/papers_archive.json').read_text())
 old=json.loads((ROOT/'docs/scholar-explorer-2026-10-28/preexisting_records.json').read_text())
 metadata={p['arxiv']:p for p in json.loads((ROOT/'docs/scholar-explorer-2026-10-28/paper_metadata.json').read_text())}
 assert papers and len(papers)<=50,'keep the selected collection bounded'
 assert len(scholars)==11 and len({s['id'] for s in scholars})==11
 assert len({p['id'] for p in papers})==len(papers),'duplicate ID'
 assert len({p['arxiv'] for p in papers})==len(papers),'duplicate paper/version'
 assert len({p['title'] for p in papers})==len(papers),'duplicate title'
 assert all(tuple(p)==REQUIRED for p in papers),'record schema/order mismatch'
 assert {p['direction'] for p in papers}==DIRECTIONS
 ids={p['id'] for p in papers};sids={s['id'] for s in scholars}
 names={s['id']:s['name'] for s in scholars}
 for p in papers:
  assert p['type'] in TYPES and 1<=len(p['tags'])<=3
  assert isinstance(p['year'],int) and 2020<=p['year']<=2026
  assert all(isinstance(p[k],str) and p[k].strip() for k in REQUIRED if k not in ('year','tags','authors','scholars'))
  assert p['authors'] and p['scholars'] and set(p['scholars'])<=sids
  assert all(names[s] in p['authors'] for s in p['scholars']),f"unverified scholar association: {p['id']}"
  m=metadata[p['arxiv']]
  assert p['title']==m['title'],'title differs from inspected primary record'
  normalized=[' '.join(a.split(', ')[::-1]) if ', ' in a else a for a in m['authors']]
  assert p['authors']==normalized,'author list differs from inspected primary record'
  for k in ('url','publication_source'):
   assert urlparse(p[k]).scheme=='https' and urlparse(p[k]).netloc
 for s in scholars:
  assert set(s['recommended'])<=ids
  assert all(s['id'] in next(p for p in papers if p['id']==i)['scholars'] for i in s['recommended'])
  assert any(s['id'] in p['scholars'] for p in papers),'uncovered scholar'
 assert not(ids & {p['id'] for p in archive}),'main/archive overlap'
 assert len({p['id'] for p in archive})==len(archive)
 all_records={p['id']:p for p in papers+archive}
 assert len(old)==58 and all(p['id'] in all_records for p in old),'old record lost'
 assert all(p['title']==all_records[p['id']]['title'] for p in old),'legacy ID reused'
 for label,array,next_label in [('PAPERS',papers,'DIRECTIONS'),('SCHOLARS',scholars,'ARCHIVE'),('ARCHIVE',archive,'ROUTE')]:
  m=re.findall(r'const '+label+r' = (\[[\s\S]*?\]);\nconst '+next_label+r' = ',html)
  assert len(m)==1 and json.loads(m[0])==array,f'{label} HTML snapshot stale'
 with (ROOT/'public/data/papers.csv').open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f);assert tuple(reader.fieldnames)==REQUIRED;rows=list(reader)
 assert len(rows)==len(papers)
 assert all(str(p[k])==r[k] for p,r in zip(papers,rows) for k in REQUIRED),'CSV differs'
 # All editorial routes, opportunities and overview links must resolve.
 refs=re.findall(r"ids:\[([^]]+)\]",html)
 for group in refs:
  assert set(re.findall(r"'([^']+)'",group))<=ids,'dangling route/opportunity reference'
 assert set(re.findall(r'data-open="([a-z0-9]+)"',html))<=ids,'dangling static paper link'
 assert 'rlhf_stats_atlas_v1' in html,'browser storage key must stay compatible'
 assert (ROOT/'public/.nojekyll').exists()
 counts={d:sum(p['direction']==d for p in papers) for d in sorted(DIRECTIONS)}
 print(f'PASS: {len(papers)} papers, {len(scholars)} scholars, {len(archive)} archive; all 58 legacy IDs retained')
 print('PASS: primary author/title associations, recommendations, editorial references, CSV/HTML snapshots')
 print(json.dumps(counts,ensure_ascii=False))
 print('LIMIT: source metadata consistency is not a full-text theorem audit or remote/browser deployment check.')
if __name__=='__main__':verify()
