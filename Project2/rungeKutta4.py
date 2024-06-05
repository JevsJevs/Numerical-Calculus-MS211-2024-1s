def rungeKutta4(a, b, h, y0, func):
    n = int((b-a)/h)
    yf = y0
    for i in range(n):
        xf = a+i*h
        k1 = h*func(xf, yf)
        k2 = h*func(xf+h/2, yf+k1/2)
        k3 = h*func(xf+h/2, yf+k2/2)
        k4 = h*func(xf+h, yf+k3)
        yf += (k1+2*k2+2*k3+k4)/6
    return yf
