# https://inf-ege.sdamgia.ru/problem?id=59694

import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n-1)
print(F(2024)-F(2021))