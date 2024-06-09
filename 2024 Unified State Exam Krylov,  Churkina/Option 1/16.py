import sys
def f(n):
    if n == 1:
        return 5
    return 2 * n + 1 + f(n - 1)
sys.setrecursionlimit(3000)
print(f(2024) - f(2022))