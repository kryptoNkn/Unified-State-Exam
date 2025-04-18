f = [int(x) for x in open('17')]
m = min(f)
arr = []

for i in range(len(f)-1):
    if f[i]%16==m or f[i+1]%16==m:
        arr.append(f[i]+f[i+1])
print(len(arr), max(arr))