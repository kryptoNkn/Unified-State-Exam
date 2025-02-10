from functools import *
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return 2 * n + f(n-1)

for i in range(1, 57694):
    f(i)
print(f(57693))
print("ответ:",(3+3+2+8+5+3+9+9+4+1)**2)






