# https://inf-ege.sdamgia.ru/problem?id=6423

def F(n):
    if n <= 2:
        return n-1
    if n > 2:
        return 3 * F(n-1) - F(n-2)
print(F(6))