import math

# 1. 计算x的值：x = 16/(√17 + 1)
sqrt17 = math.sqrt(17)
x = 16 / (sqrt17 + 1)

# 2. 代入多项式 x⁵ + 2x⁴ -17x³ -x² -17
result = x**5 + 2*(x**4) - 17*(x**3) - x**2 - 17

# 3. 输出纯数字结果，保留10位小数
print(f"多项式计算结果 = {result:.10f}")

# 可选：输出化简式对应的数值 17 - 18*√17，用来校验
check = 17 - 18 * sqrt17
print(f"代数化简校验值 = {check:.10f}")