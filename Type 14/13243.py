for x in '0123456789ABCDEFGHI':
    s = int(f"1{x}253",18) + int(f"32{x}8",18)
    if s % 7 == 0:
        print(s//7)
# 19367
