from itertools import product
k=0
for i in product('БГДНОУШ', repeat=6):
    s = ''.join(i)
    k+=1
    if k%2!=0 and s[0] != 'Б' and s.count('Н') >=2 and s.count('У') == 0:
        print(k,s)

# 117625