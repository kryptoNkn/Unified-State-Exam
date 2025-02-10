from itertools import product
k = 0
for i in product(sorted(set('АКЛМНЯ')), repeat=5):
    s = ''.join(i)
    k+=1
    if s[0]=='К' and s[1]=='М':
        print(k)
        break 
