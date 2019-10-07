#练习8.2 欧拉 改进欧拉  Runge_Kutta四阶
def func(x, y):
    return -y*(1+x*y)

def Euler():
    yi = 1
    h = 0.2
    x0 = 0
    x1 = 1
    n = round((x1-x0)/h)
    for i in range(0,n):
        xi = i * h 
        yi_1 = yi + h * func(xi, yi)
        xi_1 = xi + h
        # print("Euler: i={0,%.6f}, x={1,%.6f}, y={2,%.6f}".format(i, xi_1, yi_1))
        print("Euler: i=%.6f, x=%.6f, y=%.6f" % (i, xi_1, yi_1))
        yi = yi_1

def GaiJinEuler():
    yi = 1
    h = 0.2
    x0 = 0
    x1 = 1
    n = round((x1-x0)/h)
    for i in range(0, n):
        xi = i * h
        xi_1 = xi + h
        yp = yi + h * func(xi, yi)
        yc = yi + h * func(xi_1, yp)
        yi_1 = 1/2 * (yp + yc)
        print("GaiJinEuler: i = %.6f, x = %.6f, yp = %.6f, yc = %.6f, y = %.6f" % (i, xi_1, yp, yc, yi_1))
        yi = yi_1

def Runge_Kutta_4():
    y = 1
    h = 0.2
    x0 = 0
    x1 = 1
    n = round((x1-x0)/h)
    x = x0
    for i in range(0, n):
        k1 = func(x, y)
        k2 = func(x + 1/2 * h, y + h/2 * k1)
        k3 = func(x + 1/2 * h, y + h/2 * k2)
        k4 = func(x + h, y + h * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        print("Runge-Kutta_4: i = %.0f, x = %.6f, k1 = %.6f, k2 = %.6f, k3 = %.6f, k4 = %.6f, y = %.6f" % (i, x, k1, k2, k3, k4, y))
        

if __name__ == "__main__":
    Euler()
    GaiJinEuler()
    Runge_Kutta_4()