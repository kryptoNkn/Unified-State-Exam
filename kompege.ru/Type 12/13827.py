for n in range(3, 10001):
    s = '5' + '2' * n
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5',1)

    digit_sum = sum(int(char) for char in s)

    if digit_sum == 22:
        print(n)
        break