for x in range(2031):
    i = 6 **260+6**160+6**60-x
    s = ''
    while i > 0:
        s = str(i % 6) + s
        i//=6

    if s.count('0') == 202:
        print(x)

# 216




