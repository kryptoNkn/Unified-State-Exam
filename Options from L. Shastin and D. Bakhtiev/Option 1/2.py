print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (y <= x) and (not(w)) and z
                if f==1:
                    print(x,y,w,z)
# xwyz