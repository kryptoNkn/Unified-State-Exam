for x in '0123456789ABCDEFGHIGKLM':
    n = int(f"2{x}{x}341011",23)+int(f"220{x}4",23)+int(f"110{x}6",23)
    if n % 22 == 0:
        print(n//22)
        break