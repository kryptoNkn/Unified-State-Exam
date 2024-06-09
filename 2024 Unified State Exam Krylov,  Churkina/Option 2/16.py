import sys
def f(n):
    if n == 1:
        return 3
    return 3 * n + 2 *f(n - 1)
sys.setrecursionlimit(3000)
print(f(2024) - 4 * f(2022))

# Solution: 18210