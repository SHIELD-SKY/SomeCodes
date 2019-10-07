#例8.6 亚当姆斯预测校正算法

def func(x, y):
    return y - 2*x/y

def Runge_Kutta_4():
    y_list = []
    y = 1
    h = 0.1
    x0 = 0
    x1 = 1
    n = 4
    x = x0
    for i in range(0, 3):
        k1 = func(x, y)
        k2 = func(x + 1/2 * h, y + h/2 * k1)
        k3 = func(x + 1/2 * h, y + h/2 * k2)
        k4 = func(x + h, y + h * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        print("Runge-Kutta_4: i = %.0f, x = %.6f, k1 = %.6f, k2 = %.6f, k3 = %.6f, k4 = %.6f, y = %.6f" % (i, x, k1, k2, k3, k4, y))
        
        y_list.append(y)
    return y_list

def Adams():
    h = 0.1
    x0 = 0
    y0 = 1
    x1 = x0 + h
    x2 = x1 + h
    x3 = x2 + h
    y1, y2, y3 = Runge_Kutta_4()
    print(y1)
    for i in range(3, 10):
        yp = y3 + h/24*(55*func(x3,y3) - 59*func(x2, y2) + 37*func(x1,y1) - 9*func(x0,y0)) # y 预测
        fp = func(x3 + h, yp) # f_n+1 预测
        y = y3 + h/24*(9*fp + 19*func(x3, y3) - 5*func(x2,y2) + func(x1,y1)) # y_n+1 
        # f =  func(x3 + h, y) # f_n+1
        print("Runge-Kutta_4: i = %.0f, x = %.6f, yp = %.6f, y = %.6f" % (i, x3+h, yp, y))
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = x3 + h

        y0 = y1
        y1 = y2
        y2 = y3 
        y3 = y
        
if __name__ == "__main__":
    Adams()

