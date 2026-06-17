import math
# 方程两个根
x1 = (1 + math.sqrt(5))/2
x2 = (1 - math.sqrt(5))/2

def calc(x):
    return math.sqrt(x**8 + 7/(x**4))

print(calc(x1))
print(calc(x2))
print(4*math.sqrt(3))