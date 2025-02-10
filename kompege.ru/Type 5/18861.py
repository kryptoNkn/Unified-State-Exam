# 18861
def f3(x):
    s = ''
    while x != 0:
        s = str(x%3)+s
        x//=3
    return s

# for n in range(3, 10000):
#     troich = f3(n)
#     if troich.endswith('10'):
#         troich2 = '2' + troich
#     else:
#         troich2 = '1' + troich
#     r = int(troich2,3)
#     if r > 130:
#         print(n)
#         break

# for n in range(3, 10000):
#     troich = f3(n)
#     if troich[-2:] == '10':
#         troich2 = '2' + troich
#     else:
#         troich2 = '1' + troich
#     r = int(troich2, 3)
#     if r > 130:
#         print(n)
#         break

# for n in range(3, 10000):
#     troich = f3(n)
#     if troich[:-2:-1] == "0" and troich[-2] == '1':
#         troich2 = '2' + troich
#     else:
#         roich2 = '1' + troich
#     r = int(troich2, 3)
#     if r > 130:
#         print(n)
#         break


