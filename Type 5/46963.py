# https://inf-ege.sdamgia.ru/problem?id=46963

for n in range(2, 10000):
    s = bin(n)[2:]
    chet1 = [x for x in s[1::2] if x == "1"] # Формирование списка всех '1' на четных позициях в строке s
    nechet0 = [x for x in s[0::2] if x == "0"] # Формирование списка всех '0' на нечетных позициях в строке s
    r = abs(len(chet1) - len(nechet0)) # Вычисляем разницу между количеством '1' на четных и '0' на нечетных позициях
    if r == 5:
        print(n)
        break
    
