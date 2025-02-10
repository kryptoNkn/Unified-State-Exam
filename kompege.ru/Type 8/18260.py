from itertools import product
k = 0
for i in product('0123456789AB', repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and s.count('B') == 1 and s.count('0') + s.count('2') + s.count('4') + s.count('6') + s.count('8') + s.count('A') == s.count('1') + s.count('3') + s.count('5') + s.count('7') + s.count('9') + s.count('B'):
        k+=1
print(k)