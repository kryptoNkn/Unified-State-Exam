from itertools import product
k=0
for i in product(sorted(set("АБЗИ")), repeat=4):
    s=''.join(i)
    k+=1
    if 'ИЗБА' in s:
        print(k)
        break