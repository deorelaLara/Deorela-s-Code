import math
#import math as m 

def coseno(x, n):
    n= 6
    cosApprox = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cosApprox += ( coef ) * ( (num)/(denom) )
    return cosApprox


angle_rad = (math.radians(45))
print(angle_rad)
out = coseno(angle_rad,6)
print(out)
print('#####')
print(math.pi/4)
print(math.radians(math.pi/4))

"""
x=45
k=0
N=6
s=0
sign=1.0

while k<N: 
    term=sign*x**(k)/m.factorial(k)
    s=s+term
    k += 2
    sign = -sign

print(s)

"""