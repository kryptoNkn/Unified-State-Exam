def f(n):
    if n==1 or n==2: return 1
    if n>2 and n%2==0: return (n*f(n-1))//2
    else:
        return (n*f(n-1)+f(n-2))//3
print(f(13))