print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(x <= y)) or (z==w) or z
                if f==0: print(x,y,w,z)
# zyxw