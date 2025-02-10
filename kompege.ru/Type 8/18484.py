from itertools import product
k = 0
for i in product(sorted(set('ПАВСИКАКИЙ')), repeat = 6):
    s = ''.join(i)
    if 'АА' in s or 'ИИ' in s or 'АИ' in s or 'ИА' in s:
        k+=1
        if 'КАКААА' in s:
            print(k)

