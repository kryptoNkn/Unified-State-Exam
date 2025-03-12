def chetv(x):
    s=''
    while x!=0:
        s = str(x%4)+s
        x//=4
    return s


s = 4**644 + 4**322 + 16**35 - 64**3
c = chetv(s)
print(c.count('3'))