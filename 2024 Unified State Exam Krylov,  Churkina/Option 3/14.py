for x in '0123456789ABCDEFGHIGKLMNO':
    n = int(f"1{x}2{x}3{x}4{x}5",25) + int(f"2{x}024",25) + int(f"1{x}099",25)
    if n % 24 == 0:
        print(n//24)

# 11727433732