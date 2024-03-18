def bissection(func, a, b, iter):
    left = a
    right = b
    for i in range(iter):
        x = (left+right)/2

        fa = func(left)
        fx = func(x)
        fb = func(right)

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