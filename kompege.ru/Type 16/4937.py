# https://inf-ege.sdamgia.ru/problem?id=4937

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >2:
        return F(n-2)*(n-1)
print(F(7))

