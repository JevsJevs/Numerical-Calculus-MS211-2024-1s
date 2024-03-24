import math

x_barra = 3.6037349
error = 0.000001

#Constants
Alpha = 0.2
Euler = math.e

def derived_func(x):
    return Alpha*(Euler**(Alpha * x)) - (Alpha - 1)*(Euler**((Alpha - 1) * x))

def zero_func(fa, ga, a):
    return a - (fa/ga)

def calc_error(x, x_barra):
    return abs(x - x_barra)/x_barra

def newton(func, a, iter = 0):
    fa = func(a)
    ga = derived_func(a)

    if calc_error(a, x_barra) < error:
        return a, iter

    else:
        a = zero_func(fa, ga, a)
        iter += 1

        a, iter = newton(func, a, iter)
        return a, iter