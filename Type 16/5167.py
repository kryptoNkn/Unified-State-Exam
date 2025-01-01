from functools import lru_cache
@lru_cache(None)
def f(n):
    if n >= 10000: return n
    if n < 10000 and n%2==0: return f(n+2)-3
    return f(n+2)+1

for i in range(10000, 0, -1):
    f(i)
print(f(94)-f(80))