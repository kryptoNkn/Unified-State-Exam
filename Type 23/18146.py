def f(x, y):
    if x < y: return 0
    if x == y: return 1
    if x == 28: return 0
    return f(x - 3, y) + f(x // 3,y) + f(x//2,y)
from_46_to_20 = f(46,20)
from_20_to_3 = f(20,3)
print(from_46_to_20*from_20_to_3)