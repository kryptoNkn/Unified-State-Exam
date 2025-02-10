for x in '0123456789ABCDEFGHIJKL':
    s = int(f"A23{x}AC0",22) + int(f"GB{x}21670",22)
    if s % 21 == 0:
        print(s//22)