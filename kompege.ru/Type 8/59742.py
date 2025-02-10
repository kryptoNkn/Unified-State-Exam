# https://inf-ege.sdamgia.ru/problem?id=59742

from itertools import permutations
alphabet = '0123456789'
arr = []
for i in permutations(alphabet, 4):
    num = ''.join(i)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1').replace('9','1')
        if '11' not in num and '22' not in num:
            arr.append(i)
print(len(arr))