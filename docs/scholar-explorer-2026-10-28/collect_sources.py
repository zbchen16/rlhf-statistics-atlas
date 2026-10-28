"""Read-only HTTP collection; saves public source metadata inside this task folder."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import json, urllib.request, re
ROOT=Path(__file__).resolve().parent
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.text=[]; self.links=[]; self.meta={}; self.link=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta': self.meta.setdefault(a.get('name',a.get('property','')),[]).append(a.get('content',''))
  if tag=='a': self.link=[a.get('href',''),'']
 def handle_endtag(self,tag):
  if tag=='a' and self.link: self.links.append(self.link); self.link=None
 def handle_data(self,s):
  self.text.append(s)
  if self.link:self.link[1]+=s

def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research bibliography verification)'})
 raw=urllib.request.urlopen(req,timeout=25).read().decode('utf-8','replace'); p=Page();p.feed(raw)
 return {'url':url,'accessed':'2026-10-28','meta':p.meta,'text':' '.join(' '.join(p.text).split()),'links':p.links}
if __name__=='__main__':
 urls={
 'shi':'https://callmespring.github.io/publication','xiao':'https://jiancongxiao.github.io/publications/',
 'sun':'https://web.ics.purdue.edu/~sun244/research.html','zhang':'https://www.tongzhang-ml.org/publication',
 'liu':'https://lsjxjtu.github.io/publications.html','tang':'https://haorantang.github.io/',
 'wang':'https://qizhouwang.github.io/homepage/','yang':'https://puning97.github.io/',
 'bao':'https://baoguangsheng.github.io/publications/','wu':'https://daftstone.github.io/',
 'li':'https://lx10077.github.io/publications/'}
 def run(kv):
  k,u=kv
  try:
   d=fetch(u); (ROOT/'sources').mkdir(exist_ok=True); (ROOT/'sources'/f'{k}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
   return k,[(u,t.strip()) for u,t in d['links'] if re.search('arxiv|proceedings|openreview|doi.org|tandfonline',u)]
  except Exception as e:return k,str(e)
 with ThreadPoolExecutor(max_workers=6) as ex:
  for k,r in ex.map(run,urls.items()):print(k,json.dumps(r,ensure_ascii=False))
