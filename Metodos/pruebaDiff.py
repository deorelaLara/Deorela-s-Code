import numpy as np
import sympy as sym 

x , y = sym.symbols('x y')

print(2*x + 3*x -y)
print(sym.diff(x**2, x))
"""    
# Fibonacci Sequence with first 8 numbers
fibs = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21])
diff_fibs = np.diff(fibs)
print(diff_fibs)
# [1 0 1 1 2 3 5 8]
"""