def f(s1,s2,m):
    if s1+s2 >= 65: return m%2==0
    if m==0: return 0
    h = [f(s1+1,s2,m-1),f(s1,s2+1,m-1),f(s1*3,s2,m-1),f(s1,s2*3,m-1)]
    # return any(h) if m%2!=0 else any(h)
    return any(h) if m % 2 != 0 else all(h)
# print(min([s for s in range(1,58) if not f(6,s,1) and f(6,s,2)]))
print([s for s in range(1,58) if not f(6,s,1) and f(6,s,3)])
print([s for s in range(1,58) if f(6,s,4) and not f(6,s,2)])