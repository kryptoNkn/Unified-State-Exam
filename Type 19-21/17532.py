def f(a,b,m):
    if a + b>=65: return m%2==0
    if m == 0: return 0
    h = [f(a+1,b,m-1), f(a*3,b,m-1), f(a, b+1, m-1), f(a, b*3,m-1)]
    return any(h) if (m-1)%2==0 else any(h)
print([s for s in range(1, 300) if f(6,s,2)])
print([s for s in range(1, 300) if not f(6,s,1) and f(6,s,3)])
print([s for s in range(1, 300) if f(6,s,4) and not f(6,s,2)])