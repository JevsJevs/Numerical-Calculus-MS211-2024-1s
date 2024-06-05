def euller(a, b, h, y0, func):
    list = []
    n = int((b-a)/h)
    list.append((a, y0))
    yf = y0
    for i in range(n):
        xf = a+(i+1)*h
        yf += h*func(a+i*h, yf)
        list.append((xf, yf))
    return list