from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <3: return n
    if n>2: return n-1+f(n-1)
for i in range(5000):
    f(i)
print(f(4044))