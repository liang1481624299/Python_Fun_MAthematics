import math

# 定义方程 f(x) = x*lnx - (x+54)*ln3
def f(x):
    return x * math.log(x) - (x + 54) * math.log(3)

# 遍历整数试根
for x in range(1, 100):
    if abs(f(x)) < 1e-10: # 浮点误差判定
        print(f"方程的解 x = {x}")
        break
        