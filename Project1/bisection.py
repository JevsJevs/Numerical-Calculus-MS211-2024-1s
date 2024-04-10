import sys
import error as err
    
def bisection(func, a, b, iter, error):
    left = a
    right = b

    relError = sys.maxsize
    prevX = sys.maxsize
    for i in range(iter):
        x = (left+right)/2

        fa = func(left)
        fx = func(x)
        fb = func(right)

        if isinstance(error, err.absoluteError) and abs(fx) < error.error:
            break
        elif isinstance(error, err.relativeError) and i > 0:
            relError = abs(x-prevX)/abs(x)
            if relError < error.error:
                break

        prevX = x

        if fa*fx < 0:
            right = x
        elif fb*fx < 0:
            left = x
        elif fx == 0:
            #In case x is found precisely
            return x
        else:
            #Bissection unapplicable
            return False
        
    return x