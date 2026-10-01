# -*- coding: utf-8 -*-
"""删除 resources-data.py 中最后追加的重复 wikipedia-elon-musk 条目。"""
import io

p = 'tools/resources-data.py'
s = io.open(p, encoding='utf-8').read()
j = s.rfind('"id": "wikipedia-elon-musk"')
assert j > 0
start = s.rfind('    {', 0, j)
assert start > 0
end = s.find('    },\n', j)
assert end > 0
s = s[:start] + s[end + len('    },\n'):]
assert s.count('"id": "wikipedia-elon-musk"') == 1, s.count('"id": "wikipedia-elon-musk"')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('dupe removed; entries now:', s.count('"id": "'))
