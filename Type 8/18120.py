from itertools import product
k = 0
num = 0
for i in product(sorted(set('ПРЕСТОЛ')), repeat = 5):
    s = ''.join(i)
    num+=1
    if num % 2 != 0 and (s[-1] == 'Е' or s[-1] == 'О') and s.count('П')+s.count('Р')+s.count('С')+s.count('Т')+s.count('Л')<=3:
        k+=1
print(k)