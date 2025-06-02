def f(s1,s2,m):
    if s1+s2 <= 72: return m%2==0
    if m==0: return 0
    h = [f(s1-3,s2,m-1),f(s1,s2-3,m-1),f(s1//2+s1%2,s2,m-1),f(s1,s2//2+s2%2,m-1)]
    # return any(h) if m%2!=0 else any(h)
    return any(h) if m % 2 != 0 else all(h)
# print(max([s for s in range(23, 1000) if f(50,s,2)]))
print([s for s in range(23,1000) if not f(50,s,1) and f(50,s,3)])
print([s for s in range(23,1000) if f(50,s,4) and not f(50,s,2)])