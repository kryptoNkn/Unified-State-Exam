def f(s,m):
    if s < 222: return m%2==0
    if m == 0: return 0
    h = [f(s-2,m-1), f(s-5, m-1), f(s//2,m-1)]
    return any(h) if m%2!=0 else all(h)
print(max([s for s in range(222, 10000) if not f(s,1) and f(s,2)]))
print([s for s in range(222, 10000) if not f(s,1) and f(s,3)])
print([s for s in range(222, 10000) if f(s,4)])