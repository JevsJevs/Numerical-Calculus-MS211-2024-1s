import sys
import error as err

def zero_func(fa, ga, a):
    return a - (fa/ga)

def calc_error(x, x_barra):
    return abs(x - x_barra)/x_barra

def newton(func, d_func, a, iter, error):
    relError = sys.maxsize
    prevX = sys.maxsize

    i = 0
    while i < iter:
        fa = func(a)
        ga = d_func(a)

        if isinstance(error, err.absoluteError) and abs(fa) < error.error:
            return a, i

        elif isinstance(error, err.relativeError):
            if i > 0:
                relError = abs(a - prevX) / abs(a)
                if relError < error.error:
                    return a, i

        prevX = a

        a = zero_func(fa, ga, a)
        i += 1