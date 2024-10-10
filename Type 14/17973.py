for x in '0123456789abcdefghijklm':
    n = int(f"12{x}734", 24) + int(f"8{x}95{x}3", 24) + int(f"24{x}796", 24)

    if n % 23 == 0:
        quotient = n // 23
        print(quotient)