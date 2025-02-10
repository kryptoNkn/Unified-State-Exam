from itertools import product
k = 0
for i in product(sorted(set('КОМПЬЮТЕР')),repeat = 5):
    s = ''.join(i)
    k+=1
    if s[0] != 'Ь' and s.count('К') == 2 and k % 2 != 0:
        print(k)

#58979

