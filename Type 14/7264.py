x = 343**515-6*49**520+5*49**510-3*7**530-550
count = 0
while x != 0:
    if x % 7 == 6:
        count += 1
    x //= 7
print(count)