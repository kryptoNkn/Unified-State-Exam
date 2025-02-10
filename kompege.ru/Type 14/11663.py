for x in range(27):
    n = int(f"17{x}35",27) + int(f"{x}742M",27) + x**3
    if n % 23 == 0:
        print(n//23)