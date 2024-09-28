x = 4 **644 +4**322+16**35-64**3
count = 0
while x > 0:
    if x % 4 == 3:
        count += 1
    x//=4
print(count)