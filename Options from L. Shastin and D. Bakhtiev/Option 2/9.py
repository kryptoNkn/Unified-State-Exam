f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    chetn = [int(x) for x in a if x%2==0]
    ne_chetn = [int(x) for x in a if x % 2 != 0]
    a.sort()
    if a[-1] < a[0]+a[1]+a[2]:
        if sum(chetn) == sum(ne_chetn):
            k+=1
print(k)