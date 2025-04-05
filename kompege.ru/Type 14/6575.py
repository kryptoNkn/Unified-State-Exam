n = 766**66+15**13-22
k=0
while n!=0:
    if n%13==12:
        k+=1
    n//=13
print(k)
