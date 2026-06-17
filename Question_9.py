import math

# 对数变形后的目标函数，避免超大指数溢出
def f(x):
    # x^5 * lnx - ln(3375) = 0
    return (x**5) * math.log(x) - math.log(3375)

# 二分法求根，区间1~10
left = 1.0
right = 10.0
# 迭代50次提高精度
for _ in range(50):
    mid = (left + right) / 2
    val = f(mid)
    if val < 0:
        left = mid
    else:
        right = mid

x_sol = (left + right) / 2
print(f"方程 x^(x^5) = 3375 的数值解 x ≈ {x_sol:.10f}")

# 校验：把解代回对数等式验证
check = (x_sol**5)*math.log(x_sol)
print(f"校验值 x^5·lnx = {check:.10f}")
print(f"ln3375 = {math.log(3375):.10f}")