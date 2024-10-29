def f(x, y):
    if  x < y: return 0
    if x == y: return 1
    sqrtr_x = int(x**0.5)
    return f(x-4,y) + f(x-7,y)+f(sqrtr_x, y)
print(f(44,22) * f(22,3))