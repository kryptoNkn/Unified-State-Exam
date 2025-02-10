# https://inf-ege.sdamgia.ru/problem?id=26982

from itertools import permutations
alphabet = '01234567'
arr = []
for i in permutations(alphabet, 5):
    num = ''.join(i)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1')
        if '11' not in num and '22' not in num:
            arr.append(i)
print(len(arr))

