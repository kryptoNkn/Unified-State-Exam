#https://inf-ege.sdamgia.ru/problem?id=59846

def f(x,y):
    if x < y: return 0
    if x== y: return 1
    else: return f(x-2, y) + f(x-3, y) + f(x//3, y)
print(f(20,3))