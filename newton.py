e = 0.00001

xs = []
xs.append((1.2,1.2))

def f(x1,x2):
    return(100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2)

def grad_k(x1,x2):
    g_k1 = 400 * (x1 ** 3 - x1 * x2) + 2 * (x1 - 1)
    g_k2 = 200 * (x2 - x1 ** 2)
    return(g_k1,g_k2)

def laplace_k(x1,x2):
    l_k1 = (1200 * x1 ** 2 - 400 * x2 + 2 , -400 * x1)
    l_k2 = (-400 * x1, 200)
    return(l_k1,l_k2)

while(True):
    x1,x2 = xs[-1]
    g = grad_k(x1,x2)
    d = (-g[0],-g[1])
    L = laplace_k(x1,x2)
    if (g[0] ** 2 + g[1] ** 2) <= e ** 2:
        print("steps: " + str(len(xs)-1))
        print("optimal solution: "+str(x1) + " " + str(x2))
        break
    det = L[0][0] * L[1][1] - L[0][1] * L [1][0]
    d = ((d[0] * L[1][1] - d[1] * L[1][0]) / det, (-d[0] * L[0][1] + d[1] * L[0][0]) / det)
    xs.append((x1 + d[0], x2 + d[1]))
