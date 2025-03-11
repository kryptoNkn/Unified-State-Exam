def f(x,y,s):
    if x < y: return 0
    if x == y: return 1
    if x==28: return 0
    else:
        if x%2==0:
            return f(x-2,y,s+'A')+f(x//2,y,s+'B')
        else:
            return f(x-2,y,s+'A')+f(x-3,y,s+'B')
print(f(98,1,''))