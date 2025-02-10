import itertools
count = 0
for i in set(itertools.permutations('КАРПЫ', 5)):
    s = ''.join(i)
    if s[0] != 'Р' and s[-1] != 'Р':
        s = s.replace('А', '*')
        s = s.replace('Ы', '*')
        if '**' not in s:
            count += 1
print(count)