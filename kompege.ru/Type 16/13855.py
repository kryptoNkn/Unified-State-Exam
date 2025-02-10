import sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 7777:
        return n
    if n < 7777:
        return n+5+f(n+5)
print(f(1101)-f(1111))