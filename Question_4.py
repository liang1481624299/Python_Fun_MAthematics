import math

# 计算常数
sqrt6 = math.sqrt(6)
sqrt11 = math.sqrt(11)

# 方程两个根
x1 = -sqrt6 + sqrt11
x2 = -sqrt6 - sqrt11

# 分别计算两个根的立方值
x1_3 = x1 ** 3
x2_3 = x2 ** 3

# 保留10位小数输出纯数字结果
print(f"第一个根 x = -√6 + √11，x³ = {x1_3:.10f}")
print(f"第二个根 x = -√6 - √11，x³ = {x2_3:.10f}")