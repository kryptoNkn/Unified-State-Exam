from itertools import product

k = 0
for i in product('АЙЛМ', repeat = 5):
    s = ''.join(i)
    k+=1
    if 'М' not in s and 'Л' not in s and 'ЙЙ' not in s:
        print(k)

# 274

