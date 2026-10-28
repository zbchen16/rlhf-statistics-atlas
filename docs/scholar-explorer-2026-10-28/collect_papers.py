from collect_sources import fetch,ROOT
from concurrent.futures import ThreadPoolExecutor
import json,re,time
c=json.loads((ROOT/'candidates.json').read_text())
def run(row):
 aid,scholars=row;p=ROOT/'sources'/f'arxiv-{aid}.json'
 if p.exists():d=json.loads(p.read_text())
 else:
  for attempt in range(3):
   try:
    d=fetch('https://arxiv.org/abs/'+aid);p.write_text(json.dumps(d,ensure_ascii=False,indent=2));break
   except Exception as e:
    if attempt==2:return {'arxiv':aid,'error':str(e)}
 m=d['meta'];s=d['text'];mt=re.search(r'Abstract:(.*?)\s*(?:Comments:|Subjects:|Cite as:)',s)
 return {'arxiv':aid,'scholars':scholars.split(','),'title':m.get('citation_title',[''])[0], 'authors':m.get('citation_author',[]),'date':m.get('citation_date',[''])[0],'abstract':mt.group(1) if mt else m.get('og:description',[''])[0], 'status_excerpt':s[s.find('Comments:'):s.find('Submission history')][-1500:] if 'Comments:' in s else ''}
with ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(run,c))
(ROOT/'paper_metadata.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for x in r:print(json.dumps(x,ensure_ascii=False))
