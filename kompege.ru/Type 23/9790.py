def f(x,y):
    if x<y: return 0
    if x==y: return 1
    if x==9: return 0
    if x==16: return 0
    return f(x-1,y)+f(x-2,y)+f(x//3,y)
print(f(19,3))