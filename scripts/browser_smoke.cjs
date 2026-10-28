// Run against an isolated browser context; never touches the user's browser storage.
const { chromium } = require('playwright');
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const base=process.env.ATLAS_TEST_URL||'http://127.0.0.1:8766/';
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.ATLAS_BROWSER_BIN||undefined});
 const context=await browser.newContext({viewport:{width:1440,height:1000},acceptDownloads:true});
 const page=await context.newPage();const errors=[];const checks=[];
 page.on('pageerror',e=>errors.push(e.message));
 async function check(name,fn){await fn();checks.push(name);console.log('PASS',name)}
 try{
 await page.goto(base,{waitUntil:'networkidle'});
 await check('40 papers / 3 directions',async()=>{assert.equal(await page.locator('#metric-all').innerText(),'40');assert.equal(await page.locator('#direction-cards article').count(),3)});
 await page.locator('[data-page="scholars"]').click();
 await check('11 scholar cards and author-specific recommendations',async()=>{assert.equal(await page.locator('#scholars article').count(),11)});
 await page.locator('#scholars [data-scholar="li"]').click();
 await check('scholar navigation → 5 Xiang Li papers',async()=>{assert.equal(await page.locator('#result-num').innerText(),'5');assert.match(await page.locator('#active-scholar').innerText(),/Xiang Li/)});
 await page.selectOption('#filter-year','2025');await page.selectOption('#filter-type','Theory + Method');
 await check('combined scholar/year/type filters',async()=>{assert.equal(await page.locator('#result-num').innerText(),'2')});
 await page.locator('#clear-filters').click();await page.locator('#search').fill('Chengchun Shi');
 await check('full author name search',async()=>{assert.equal(await page.locator('#result-num').innerText(),'9')});
 await page.locator('#clear-filters').click();await page.locator('[data-query="Paraphrase"]').click();
 await check('paraphrase shortcut stays in detection direction',async()=>{const dirs=await page.evaluate(()=>filtered().map(p=>p.direction));assert(dirs.length>0&&dirs.every(x=>x==='Watermark & AI Text Detection'))});
 await page.locator('#clear-filters').click();await page.locator('#papers [data-open="p01"]').first().click();
 await check('paper detail: authors, publication state, six questions',async()=>{assert.equal(await page.locator('#modalbody .info-row').count(),6);assert.match(await page.locator('#modalbody').innerText(),/Chengchun Shi/);assert.match(await page.locator('#modalbody').innerText(),/发表状态/)});
 await page.locator('#modal-star').click();await page.locator('#modal-read').click();await page.locator('#modal-note').fill('QA note <literal> 双重稳健');
 await page.reload({waitUntil:'networkidle'});await page.evaluate(()=>openPaper('p01'));
 await check('favorites, read status and notes persist across reload',async()=>{assert.match(await page.locator('#modal-star').innerText(),/已收藏/);assert.match(await page.locator('#modal-read').innerText(),/已读/);assert.equal(await page.locator('#modal-note').inputValue(),'QA note <literal> 双重稳健')});
 await page.locator('#modal-compare').click();await page.locator('#close-dialog').click();
 await page.evaluate(()=>openPaper('s241113868'));await page.locator('#modal-compare').click();await page.locator('#close-dialog').click();await page.locator('#compare-open').click();
 await check('comparison matrix includes publication state and evidence',async()=>{assert.equal(await page.locator('.compare-table thead th').count(),3);assert.match(await page.locator('.compare-table').innerText(),/发表状态/);assert.match(await page.locator('.compare-table').innerText(),/证据与局限/)});
 await page.locator('#close-dialog').click();await page.locator('#compare-clear').click();
 await page.evaluate(()=>{const s=JSON.parse(localStorage.getItem('rlhf_stats_atlas_v1'));s.p02={star:true,read:true,note:'legacy note kept'};localStorage.setItem('rlhf_stats_atlas_v1',JSON.stringify(s))});
 await page.reload();await page.locator('[data-page="explorer"]').click();await page.locator('#show-shelf').click();
 await check('archived paper keeps original title, bookmark/read state and editable note',async()=>{assert.match(await page.locator('#archived-notes').innerText(),/Understanding the Performance Gap/);assert.equal(await page.locator('[data-legacy-note="p02"]').inputValue(),'legacy note kept');await page.locator('[data-legacy-note="p02"]').fill('legacy note updated');const s=await page.evaluate(()=>JSON.parse(localStorage.getItem('rlhf_stats_atlas_v1')));assert.equal(s.p02.note,'legacy note updated');assert(s.p02.star&&s.p02.read)});
 const notesDownload=page.waitForEvent('download');await page.locator('#export-notes').click();const noteFile=await (await notesDownload).path();
 await check('notes export includes archived and current entries',async()=>{const j=JSON.parse(fs.readFileSync(noteFile,'utf8'));assert(j.records.p01.note&&j.records.p02.note)});
 await page.locator('#show-shelf').click();const csvDownload=page.waitForEvent('download');await page.locator('#download-csv').click();const csvPath=await (await csvDownload).path();
 await check('CSV export contains 40 records and author metadata',async()=>{const csv=fs.readFileSync(csvPath,'utf8');assert.equal(csv.trim().split(/\r?\n/).length,41);assert.match(csv,/authors/);assert.match(csv,/Xiang Li/)});
 await page.locator('[data-page="roadmap"]').click();
 await check('reading roadmap and downloadable plan',async()=>{assert.equal(await page.locator('#weeks .week').count(),4);const d=page.waitForEvent('download');await page.locator('#export-route').click();const f=await (await d).path();assert.match(fs.readFileSync(f,'utf8'),/Robust Detection of Watermarks/)});
 await page.locator('[data-page="ideas"]').click();
 await check('7 research opportunities with valid paper links',async()=>{assert.equal(await page.locator('#ideas .idea').count(),7);const ids=await page.locator('#ideas [data-open]').evaluateAll(xs=>xs.map(x=>x.dataset.open));assert(await page.evaluate(ids=>ids.every(id=>PAPERS.some(p=>p.id===id)),ids))});
 await page.locator('[data-page="overview"]').click();
 await page.screenshot({path:path.join(root,'docs/screenshots/scholar-desktop.png'),fullPage:true});
 await page.locator('[data-page="scholars"]').click();await page.screenshot({path:path.join(root,'docs/screenshots/scholar-map.png'),fullPage:true});
 await page.setViewportSize({width:390,height:844});await page.evaluate(()=>switchPage('overview'));
 await check('mobile menu and no horizontal overflow',async()=>{assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.locator('#menu-toggle').click();assert(await page.locator('#sidebar').evaluate(x=>x.classList.contains('open')));await page.locator('[data-page="explorer"]').click();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth))});
 await page.locator('#clear-filters').click();await page.locator('#papers [data-open="p01"]').first().click();
 await check('mobile detail fits viewport',async()=>{const b=await page.locator('.dialog').boundingBox();assert(b.width<=390&&b.x>=0)});
 await page.locator('#close-dialog').click();await page.evaluate(()=>switchPage('overview'));await page.screenshot({path:path.join(root,'docs/screenshots/scholar-mobile.png'),fullPage:true});
 await check('zero JavaScript runtime errors',async()=>assert.deepEqual(errors,[]));
 fs.writeFileSync(path.join(root,'docs/scholar-explorer-2026-10-28/browser_results.json'),JSON.stringify({date:'2026-10-28',url:base,checks,errors,status:'PASS'},null,2));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
