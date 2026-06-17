import math

# 已知 12^m = 18，解出m
m = math.log(18, 12)

# 计算指数 (2m-1)/(m-2)
exp = (2 * m - 1) / (m - 2)

# 计算 2 的该指数次方
res = 2 ** exp

# 输出结果，保留10位小数
print(f"m = {m:.10f}")
print(f"指数 (2m-1)/(m-2) = {exp:.10f}")
print(f"2^((2m-1)/(m-2)) = {res:.10f}")