def f(s1,s2,m):
    if s1+s2 >= 81: return m%2==0
    if m==0: return 0
    h = [f(s1+1,s2,m-1), f(s1,s2+1,m-1),f(s1*2,s2,m-1),f(s1,s2*2,m-1)]
    # return any(h) if m%2!=0 else any(h)
    return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(1,73) if not f(7,s,1) and f(7,s,2)])
print([s for s in range(1,73) if not f(7,s,1) and f(7,s,3)])
print([s for s in range(1,73) if f(7,s,4) and not f(7,s,2)])