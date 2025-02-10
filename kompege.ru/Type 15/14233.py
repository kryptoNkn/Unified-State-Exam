# https://inf-ege.sdamgia.ru/problem?id=14233

arr = []
P = [i for i in range(17,47)]
Q = [i for i in range(22,58)]
for Amin in range(1, 100):
    for Amax in range(1 + Amin, 100):
         A = [i for i in range(Amin,Amax)]
         flag = True
         for x in range(-100,100):
             if (not(not(x in A)) <= (((x in P) and (x in Q)) <= (x in A))):
                  flag = False
         if flag == True:
             m = Amax - Amin
             arr.append(m)
print(min(list)-1)


