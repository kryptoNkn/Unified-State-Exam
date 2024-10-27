from itertools import product
k = 0
for i in product('АКМСУ', repeat = 5):
    k+=1
    s = ''.join(i)
    if s == 'КУМАС':
        print(k)