a0, e, r, c1 = 1, 0.00001, 0.5, 0.5

xs = []
xs.append((1.2,1.2))

def f(x1,x2):
    return(100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2)

def grad_k(x1,x2):
    g_k1 = 400 * (x1 ** 3 - x1 * x2) + 2 * (x1 - 1)
    g_k2 = 200 * (x2 - x1 ** 2)
    return(g_k1,g_k2)

while(True):
    x1,x2 = xs[-1]
    g = grad_k(x1,x2)
    d = (-g[0],-g[1])
    if (g[0] ** 2 + g[1] ** 2) <= e ** 2:
        print("steps: " + str(len(xs)-1))
        print("optimal solution: "+str(x1) + " " + str(x2))
        break
    a = a0
    while(True):
        if f(x1 + a * d[0], x2 + a * d[1]) <= f(x1,x2) + c1 * a * (g[0]*d[0] + g[1] * d[1]):
            break
        a *= r
    xs.append((x1 + a * d[0], x2 + a * d[1]))
