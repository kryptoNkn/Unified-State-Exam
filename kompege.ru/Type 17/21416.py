f = [int(x) for x in open('17')]
arr = []

for i in range(len(f)-2):
    if max(f[i],f[i+1],f[i+2])*min(f[i],f[i+1],f[i+2])>sum([int(x) for x in f if x<0]):
        arr.append(f[i]+f[i+1]+f[i+2])
print(len(arr), max(arr))