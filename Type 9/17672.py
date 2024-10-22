file = open('9')
k = 0
for string in file:
    a = [int(x) for x in string.split()]
    a.sort()
    if a[0] + a[-1] < a[1] + a[2]:
        k+=1
print(k)