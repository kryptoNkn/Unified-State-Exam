file = open('9')
k = 0
for str in file:
    a = [int(x) for x in str.split()]
    a.sort()
    if a[0] + a[-1] <= a[1] + a[2]:
        k+=1
print(k)