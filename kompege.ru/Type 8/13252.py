import itertools
count = 0
for i in set(itertools.permutations('КИДАЛА', 5)):
    s = ''.join(i)
    if 'КК' not in s and 'ИИ' not in s and 'ДД' not in s and 'АА' not in s and 'ЛЛ' not in s:
        count += 1
print(count)