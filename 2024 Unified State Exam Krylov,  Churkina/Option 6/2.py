print("x y z w F")
for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = y and (x <= w) and ((not(x)) <= ((not(w)) == z))
                print(x,y,z,w, int(f))