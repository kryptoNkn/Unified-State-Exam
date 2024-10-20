from itertools import permutations
k = 0
for i in set(permutations('0123456789ABCDEF',3)):
    s = ''.join(i)
    if s[0]!= '0':
        for j in '02468ACE':
            s = s.replace(j, '*')
        for a in '13579BDF':
            s = s.replace(a, '%')
        if '**' not in s and '%%' not in s:
            k+=1
print(k)


