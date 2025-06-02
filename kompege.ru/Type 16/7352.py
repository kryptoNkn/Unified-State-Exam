from functools import lru_cache
@lru_cache(None)
def f(n):
    if n<2: return 7
    if n>1: return 7*f(n-2)
for i in range(30000):
    f(i)
print(f(12950)//7**6473)