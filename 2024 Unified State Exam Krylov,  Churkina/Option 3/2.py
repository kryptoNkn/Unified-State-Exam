print("x y z w")
for w in range(0,2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not(x <= y) or (not(w)) <= (not(z)) or w):
                    print(x,y,z,w)
# Solution: zywx