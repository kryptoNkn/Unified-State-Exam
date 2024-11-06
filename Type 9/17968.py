file = open('9')
k = 0
for str in file:
    a = [int(x) for x in str.split()]
    chet = [int(x) for x in a if x % 2 == 0]
    ne_chet = [int(x) for x in a if x % 2 != 0]
    a.sort()
    if a[-1] < a[0] + a[1] + a[2]:
        if sum(chet) == sum(ne_chet):
            k+=1
print(k)