def rungeKutta4(a, b, h, y0, func):
    list = []
    n = int((b-a)/h)
    list.append((a, y0))
    yf = y0
    for i in range(n):
        x0 = a+i*h
        k1 = h*func(x0, yf)
        k2 = h*func(x0+h/2, yf+k1/2)
        k3 = h*func(x0+h/2, yf+k2/2)
        k4 = h*func(x0+h, yf+k3)
        xf = a+(i+1)*h 
        yf += (k1+2*k2+2*k3+k4)/6
        list.append((xf, yf))
    return list
