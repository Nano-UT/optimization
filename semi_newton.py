#理科I類31組2年 J4-170889 物理工学科内定 長吉 博成

import numpy as np

a0, e, r, c1 = 1, 0.00001, 0.5, 0.5

def f(x1,x2):
    return(100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2)

def grad_k(x1,x2):
    return(np.array([[400 * (x1 ** 3 - x1 * x2) + 2 * (x1 - 1)],[200 * (x2 - x1 ** 2)]]))

def laplace_k(x1,x2):
    return(np.array([[1200 * x1 ** 2 - 400 * x2 + 2 , -400 * x1],[-400 * x1, 200]]))

xs = []
Hs = []
xs.append(np.array([[1.2],[1.2]]))
x1,x2 = xs[-1][0][0],xs[-1][1][0]
L = laplace_k(x1,x2)
Hs.append(np.linalg.inv(L))

while(True):
    x1,x2 = xs[-1][0][0],xs[-1][1][0]
    H = Hs[-1]
    g = grad_k(x1,x2)
    if (g[0][0] ** 2 + g[1][0] ** 2) <= e ** 2:
        print("steps: " + str(len(xs)-1))
        print("optimal solution: "+str(x1) + " " + str(x2))
        break
    d = - np.dot(H,g)
    a = a0
    while(True):
        if f(x1 + a * d[0][0], x2 + a * d[1][0]) <= f(x1,x2) + c1 * a * (g[0][0]*d[0][0] + g[1][0]*d[1][0]):
            break
        a *= r
    xs.append(np.array([[x1 + a * d[0][0]],[x2 + a * d[1][0]]]))
    s = xs[-1] - xs[-2]
    y = grad_k(xs[-1][0][0],xs[-1][1][0]) - grad_k(x1,x2)
    H = np.dot(np.dot((np.eye(2) - np.dot(s,y.T)/np.dot(y.T,s)) , H),((np.eye(2) - np.dot(y,s.T)/np.dot(s.T,y)))) + np.dot(s,s.T) / np.dot(s.T,y)
    Hs.append(H)
