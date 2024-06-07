import math
import euler as method1
import rungeKutta4 as method2
import analytical as method3
import matplotlib.pyplot as plt
import numpy as np

# Constants:
Euler = math.e

# Parameters:
a = int(input("Tempo inicial (a): "))
b = int(input("Tempo final (b): "))
y0 = float(input("Número de indivíduos no instante inicial (y0): "))
r = float(input("Taxa de reprodução da população (r): "))
k = float(input("Constante de capacidade do meio (k): "))

# Ensure r is a divisor of (b-a) interval
while True:
    h = float(input("Número de passos (h): "))
    remainder = (b - a) % h
    if abs(remainder) < 1e-10:
        break
    elif abs(remainder - h) < 1e-10:
        h += remainder
        break
    else:
        print(f"O valor de h ({h}) não é um divisor de {b - a}. Por favor, insira um novo valor.")

n = int((b-a)/h)
t = np.linspace(a, b, 100)

# Given: f(x) => Pierre-François Equation
def pierreFrancois(t):
    return k*y0*Euler**(r*t)/(k+y0*(Euler**(r*t)-1))

# f'(x) = > Pierre-François Derived Equation
def d_pierreFrancois(t, y):
    return r*y*(1-y/k)

# Run Methods
listAnalitic = method3.analytical(a, b, h, n, y0, pierreFrancois)
listEuler = method1.euler(a, b, h, n, y0, d_pierreFrancois)
listRK = method2.rungeKutta4(a, b, h, n, y0, d_pierreFrancois)

# Last values
print('__________________\n')
print("Last Analtical Value: ", listAnalitic[-1][-1])
print("Last Euler Value: ", listEuler[-1][-1])
print("Last 4th order Runge-Kutta Value: ", listRK[-1][-1])

# Error measure
errorEuler = 0
errorRK = 0

for i in range(n):
    errorEuler += abs(listAnalitic[n][1] - listEuler[n][1])
    errorRK += abs(listAnalitic[n][1] - listRK[n][1])

print('__________________\n')
print('Euler Error: ', errorEuler)
print('4th Runge-Kutta Error: ', errorRK)

# Plot
plt.plot(*zip(*listEuler), label='Euler', color='red')
plt.plot(*zip(*listRK), label='Runge-Kutta4', color = 'green')
plt.plot(t, pierreFrancois(t), label='Analitic', color='blue')
plt.show()