def f(n):
    if n <= 1: return 1
    if n==2: return 2
    if n%3==0: return 2*n-f(n//3)-f(n-1)
    return n+f(n-2)+f(n//10)
k=0
for i in range(50,100+1):
    if 50 < f(i) <= 200:
        k+=1
print(k)