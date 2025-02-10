for x in '0123456789ABCDEFGHIJKLMNOPQ':
    s = int(f"123{x}24",27)+int(f"135{x}78",27)
    k=0
    if s %26==0:
        print(s//26)

# 1213206