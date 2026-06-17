from sympy import symbols, log, solve, simplify

# 定义符号
a, b, c, k = symbols('a b c k', positive=True)

# 由 2^a = k, 3^b = k, 6^c = k 解出a,b,c用k表示
eq1 = 2**a - k
eq2 = 3**b - k
eq3 = 6**c - k

sol_a = solve(eq1, a)[0]
sol_b = solve(eq2, b)[0]
sol_c = solve(eq3, c)[0]

print(f"a = {sol_a}")
print(f"b = {sol_b}")
print(f"c = {sol_c}")

# 构造表达式 ab/(ac+bc)
expr = (a*b) / (a*c + b*c)
# 代入a,b,c
expr_sub = expr.subs({a:sol_a, b:sol_b, c:sol_c})
# 化简
res = simplify(expr_sub)

print("\n表达式 ab/(ac+bc) 化简结果：", res)