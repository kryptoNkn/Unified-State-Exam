file = open('9')
k = 0
for str in file:
    a = [int(x) for x in str.split()]
    tri_repeat = [int(x) for x in a if a.count(x) == 3]
    non_repeat = [int(x) for x in a if a.count(x) == 1]
    repeat = [int(x) for x in a if a.count(x)>1]
    if len(set(tri_repeat)) == 1 and len(tri_repeat) == 3:
        if len(non_repeat) == 3:
            if sum(repeat) ** 2 > sum(non_repeat) ** 2:
                k+=1
print(k)