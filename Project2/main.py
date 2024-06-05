import math
import euller as method1
import rungeKutta4 as method2
import matplotlib.pyplot as plt


#parameters:
a, b = [0, 10]
r = 0.5
k = 10
h = 5
y0 = 1
Euller = math.e

#give f(x)
def func(t, y):
    return r*y*(1-y/k)

#analytic solution
def func_analitic(t):
    return k*y0*Euller**(r*t)/(k+y0*(Euller**(r*t)-1))

def list_analitic():
    list = []
    n = int((b-a)/h)
    for i in range(n+1):
        t = a+i*h
        list.append((t, func_analitic(t)))
    return list

#run methods
listEuller = method1.euller(a, b, h, y0, func)
listRK = method2.rungeKutta4(a, b, h, y0, func)
listAnalitic = list_analitic()

print(listEuller[-1][-1])
print(listRK[-1][-1])
print(listAnalitic[-1][-1])

#plot
plt.plot(*zip(*listEuller), label='Euller', color='red')
plt.plot(*zip(*listRK), label='Runge-Kutta 4', color = 'green')
plt.plot(*zip(*listAnalitic), label='Analitic', color = 'blue')
plt.show()



