for x in range(2, 2026):
    n = 5 **2025+5**200-x
    k = 0
    while n != 0:
        if n % 5 == 4:
            k+=1
        n//=5
    if k > 198:
        print(x, k)
# 1876
