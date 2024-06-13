import sys
from functools import *
@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * (n - 1) + f(n - 1) + f(n - 2)
sys.setrecursionlimit(5000)
print(f(2024) - f(2022) - 2 * f(2021) - f(2020))

# Solution: 12271520