for x in '0123456789abcde':
    n = int(f"97968{x}15",15) + int(f"7{x}233", 15)
    if n % 14 == 0:
        chastnoe = n//14
        print(chastnoe)

# 116071912