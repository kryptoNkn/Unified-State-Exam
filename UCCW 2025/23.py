def f(x,y):
    if x>y: return 0
    if x==y: return 1
    if x==56: return 0
    return f(x+3,y)+f(x+7,y)+f(x*3,y)
print(f(12,40)*f(40,72)*f(72,89))