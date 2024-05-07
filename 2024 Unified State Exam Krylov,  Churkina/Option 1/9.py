f = open('9.txt')
count = 0
for s in f:
    a = list(map(int, s.split()))
    povt, ne_povt = [], []
    for x in a:
        if a.count(x) > 1:
            povt.append(x)
        else:
            ne_povt.append(x)
    if max(a) not in povt and len(povt) == 6 and povt.count(povt[0]) == 3:
        count += 1
print(count)
