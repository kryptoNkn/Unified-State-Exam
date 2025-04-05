for x in '0123456789ABCDEFGHIJKL':
    n = int(f"18{x}89957",22)+int(f"80{x}33",22)+int(f"521{x}6",22)
    if n%21==0:
        print(x,n//21)
        break