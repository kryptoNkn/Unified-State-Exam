k=0
for x in "0123456789ABCDEFGH":
    s = int(f"11H{x}05",18)+int(f"3F{x}54{x}8",18)+int(f"G{x}{x}{x}9",18)
    if s % 14==0:
        print(x, s//14)

# 9600497

