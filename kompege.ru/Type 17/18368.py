f = open('17')
a = [int(x) for x in f]
mn7=min([x for x in a if abs(x)%10==7])
ans = []

for i in range(len(a)-2):
    if len(str(abs(a[i+1])))==5 or len(str(abs(a[i])))==5 or len(str(abs(a[i+2])))==5:
        if a[i]*a[i+1]*a[i+2]%mn7==0:
            ans.append(a[i]*a[i+1]*a[i+2])
print(len(ans), max(ans))