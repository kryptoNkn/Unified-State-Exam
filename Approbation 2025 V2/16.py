from functools import lru_cache
@lru_cache(None)
def f(n):
    if n==1: return 1
    if n>1: return n*f(n-1)

for i in range(2,2500):
    f(i)
print((f(2024)//4+f(2023))//f(2022))