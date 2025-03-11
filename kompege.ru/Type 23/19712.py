def f(x,y,s):
    if x < y: return 0
    if x==y and 'AAA' not in s and 'BBB' not in s: return 1
    else:
        if x%2==0:
            return f(x-2,y,s+'A')+f(x//2,y,s+'B')
        else:
            return f(x-2,y,s+'A')+f(x-7,y,s+'B')
print(f(40,1,''))
