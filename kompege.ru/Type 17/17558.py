f = open('17')
a = [int(x) for x in f]
kr32 = len([x for x in a if x%32==0])
ans = []

for i in range(len(a)-1):
    if a[i]<0 or a[i+1]<0:
        if a[i]+a[i+1] < kr32:
            ans.append(a[i]+a[i+1])
print(len(ans), max(ans))