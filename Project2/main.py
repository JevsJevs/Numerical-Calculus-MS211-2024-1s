import math
import euller as method1
import rungeKutta4 as method2

#parameters:
a, b = [0, 4]
r = 0.5
k = 10
h = 0.05
y0 = 1
Euller = math.e

#give f(x)
def func(t, y):
    return r*y*(1-y/k)

#analytic solution
def func_analitic(t):
    return k*y0*Euller**(r*t)/(k+y0*(Euller**(r*t)-1))

print(method1.euller(a, b, h, y0, func))
print(method2.rungeKutta4(a, b, h, y0, func))
print(func_analitic(b))



