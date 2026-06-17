import math

# 2^a = 5，换底求a
a = math.log(5, 2)
# 8^b = 0.1，换底求b
b = math.log(0.1, 8)

# 计算2a+6b
temp = 2 * a + 6 * b
# 浮点误差修正，四舍五入到整数
temp = round(temp)
# 代入原式计算2026次幂
res = (temp + 1) ** 2026

print(f"修正后结果 = {res}")