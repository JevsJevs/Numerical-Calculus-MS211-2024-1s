x_barra = 3.6037349
error = 0.000001

def zero_func(fa, fb, a, b):
    return (fb*a - fa*b)/(fb-fa)

def calc_error(x, x_barra):
    return abs(x - x_barra)/x_barra

def secant(func, a, b, iter = 0, x = 0):
    fa = func(a)
    fb = func(b)
    if calc_error(x, x_barra) < error:
        return x, iter
    else:
        x = zero_func(fa, fb, a, b)
        iter += 1
        x, iter = secant(func, b, x, iter, x)
        return x, iter