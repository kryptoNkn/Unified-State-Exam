print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not((((not(y)) <= x) <= w))) or (z <= x)
                if f==0:
                    print(x,y,w,z)
# zwyx