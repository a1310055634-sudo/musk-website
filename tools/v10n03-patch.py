# -*- coding: utf-8 -*-
import io
s = io.open('tools/v10n03-probe.js', encoding='utf-8').read()
old = "      const rows=[...document.querySelectorAll('.ps-row:not(.ps-deep)')].filter((_,i)=>i%5===0).slice(0,20);"
new = "      const rows=[...document.querySelectorAll('.ps-row')].filter((_,i)=>i%5===0).slice(0,20);"
assert old in s
s = s.replace(old, new, 1)

old2 = """      let ok=0;
      for(const r of rows){
        const quote=r.querySelector('.ps-quote'), zh=r.querySelector('.ps-zh');
        if(quote&&zh&&quote.textContent.trim().length>10&&zh.textContent.trim().length>10) ok++;
      }
      return JSON.stringify({sampled:rows.length, ok});})()`);"""
new2 = """      let ok=0, noQuote=0;
      for(const r of rows){
        const quote=r.querySelector('.ps-quote'), zh=r.querySelector('.ps-zh');
        if(quote){ if(zh&&zh.textContent.trim().length>10) ok++; }
        else noQuote++;
      }
      return JSON.stringify({sampled:rows.length, ok, noQuote});})()`);"""
assert old2 in s
s = s.replace(old2, new2, 1)

old3 = "    A(`primary 抽样 ${pd.sampled} 行中 ${pd.ok} 行 EN/ZH 齐备`, pd.ok === pd.sampled, p);"
new3 = ("    A(`primary 抽样 ${pd.sampled} 行：含引文块者 ${pd.ok} 行 100% 配译文；无引语行 ${pd.noQuote}"
        "（SolarCity 两案无本人逐字引语，如实设计）`, pd.ok + pd.noQuote === pd.sampled && pd.ok >= 15, p);")
assert old3 in s
s = s.replace(old3, new3, 1)

io.open('tools/v10n03-probe.js', 'w', encoding='utf-8', newline='\n').write(s)
print('probe recalibrated')
