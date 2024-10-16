for x in  '01234567889ABCDEFGHI':
    n = int(f"3{x}2{x}1{x}0{x}1",19) + int(f"{x}2024",19)+int(f"1{x}077",19)
    if n % 18 == 0:
        print(n//18)

# 3632718098