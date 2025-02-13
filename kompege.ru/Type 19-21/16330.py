def f(s1,s2,m):
    if s1+s2 >= 59: return m%2==0
    if m==0: return 0
    h = [f(s1+1,s2,m-1), f(s1*2,s2,m-1), f(s1,s2+1,m-1), f(s1, s2*2,m-1)]
    return any(h) if m%2!=0 else all(h) # для 19 номера вместо all написать any
print([s for s in range(1, 53) if f(5,s,2) and not f(5,s,1)])
print([s for s in range(1, 53) if not f(5,s,1) and f(5,s,3)])
print([s for s in range(1, 53) if f(5,s,4)])