import sys
sys.setrecursionlimit(10000)

def f(n):
    if n < 4: return 1
    if n >= 4: return f(n-1)+n*2
print(f(2025))