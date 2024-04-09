import math

# Constants
Alpha = 0.2
Beta = 2
Euler = math.e

def butlerVolmer(x):
    return Euler**(Alpha*x)-Euler**((Alpha-1)*x)-Beta

def zero_func(fa, fb, a, b):
    return (fb*a - fa*b)/(fb-fa) 

def calc_error_x(x_act, x_last, error):
    return abs(x_act - x_last)/abs(x_act) < error

def calc_error_y(fx, error):
    return abs(fx) < error


def secant(func, a, b, error=0.000001, error_type_x = True, iter=0, x_act=0, x_last=0):
    if error_type_x and iter>1 and calc_error_x(x_act, x_last, error):
        return x_act, iter
    elif not(error_type_x) and iter>0 and calc_error_y(func(x_act), error):
        return x_act, iter
    elif iter > 100:
        return x_act, iter
    else:
        x_last = x_act
        x_act = zero_func(func(a), func(b), a, b)
        iter += 1
        return secant(func, b, x_act, error, error_type_x, iter, x_act, x_last)

error = float(input("Type the error: "))  
type_error = input("Type 1 for error in x or 2 for error in y: ")
if type_error == "1":
    error_type_x = True
elif type_error == "2":
    error_type_x = False
secantGuess, secantIter = secant(butlerVolmer,-5,5,error, error_type_x)
print(f"Secant Guess after {secantIter} iteractions: {secantGuess}")