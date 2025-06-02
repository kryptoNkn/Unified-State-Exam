def f(s1,s2,m):
    if s1+s2 <= 100: return m%2==0
    if m==0: return 0
    h = [f(s1-3,s2-3,m-1),f(s1//2,s2,m-1),f(s1,s2//2,m-1)]
    # return any(h) if m%2!=0 else any(h)
    return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(53,1000) if f(48,s,2)])
print([s for s in range(53,1000) if not f(48,s,1) and f(48,s,3)])
print([s for s in range(53,1000) if f(48,s,4) and not f(48,s,2)])