print("x y z w")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = x and (y <= z) and ((not(y)) <= ((not(z)) == w))
                print(x,y,z,w, int(f))
                
# Solution: xzwy
