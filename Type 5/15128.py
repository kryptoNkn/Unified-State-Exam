# https://inf-ege.sdamgia.ru/problem?id=15128

for i in range(9999, 1001, -1):
    s = str(i)
    m = [int(s[0])+int(s[1]),int(s[1])+int(s[2]),int(s[2])+int(s[3])]
    m.sort()
    if m[1] == 13 and m[2] == 15:
        print(i)
        break
    