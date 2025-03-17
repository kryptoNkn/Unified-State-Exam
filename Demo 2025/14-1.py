for x in '0123456789ABCDEFGHI':
    k=0
    s = int(f"98897{x}21",19)+int(f"2{x}923",19)
    if s % 18 == 0:
        print(s//18)
# 469034148