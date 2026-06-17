import numpy as np

# 求解x^5+x+1=0的根
roots = np.roots([1,0,0,0,1,1])
for r in roots:
    # 验证根满足方程
    if abs(r**5 + r + 1) < 1e-10:
        val = r**3 - r**2
        print(f"根{r:.4f}，x³-x²={val:.4f}")