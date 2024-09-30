for x in '0123456789abcdefghigklmnopq':
    n = int(f'123{x}24', 27) + int(f'135{x}78', 27)
    if n % 26 == 0:
        print(x,n//26)
# 1213206


