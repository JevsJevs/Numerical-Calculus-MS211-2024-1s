def zero_func(fa, fb, a, b):
    return (fb*a - fa*b)/(fb-fa)

def secant(func, a, b, iter, x = 0):
    fa = func(a)
    fb = func(b)
    if iter == 0 or fa == fb:
        return x
    else:
        x = zero_func(fa, fb, a, b)
        x = secant(func, b, x, iter-1, x)
        return x