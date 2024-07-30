print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(w <= (not(x <= y)))) and ((not(x)) <= ((not(y)) == z))
                print(x,y,z,w, int(f))