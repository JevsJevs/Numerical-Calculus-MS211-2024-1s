def euller(a, b, h, y0, func):
    n = int((b-a)/h)
    yf = y0
    for i in range(n):
        xf = a+i*h
        yf += h*func(xf, yf)
    return yf
