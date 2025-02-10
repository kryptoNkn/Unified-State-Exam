for x in "0123456789ABCDEFGHIJKL":
    s = int(f"56{x}C20", 22) + int(f"89F{x}2",22) + int(f"H24{x}K21",22)
    if s % 21 == 0:
        print(s//21)
# 93708051