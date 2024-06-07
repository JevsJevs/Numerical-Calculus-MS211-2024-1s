def analytical(a, b, h, n, y0, func):
    list = []
    list.append((a, y0))
    yf = y0
    for i in range(n):
        xf = a+ (i+1)*h
        yf = func(xf)
        list.append((xf, yf))
    return list