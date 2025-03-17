def f(n):
    if n==1: return 1
    if n==2: return 1
    if n>2 and n%2==0: return f(n-2)+f(n-3)+10
    if n>2 and n%2!=0: return f(n-1)+f(n-2)
print(f(22))