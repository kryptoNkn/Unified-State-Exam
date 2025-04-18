f = [int(x) for x in open('17')]
okonc7 = [int(x) for x in f if abs(x)%10==7]
arr = []

for i in range(len(f)-1):
    if (f[i]<0 and f[i+1]>0) or (f[i]>0 and f[i+1]<0):
        if f[i]+f[i+1]<len(okonc7):
            arr.append(f[i]+f[i+1])
print(len(arr), max(arr))