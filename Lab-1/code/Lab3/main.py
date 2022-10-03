import matplotlib.pyplot as plt
import intvalpy as iv
import numpy as np

from funcs import threeHumpCamelFunc, himmelblausFunc, booth, himmelblausFunc_1, booth_1

import copy

EPS = 0.01

def plotTrace(func, trace, x_int, y_int):
    x = np.mgrid[x_int[0]:x_int[1]:300j]
    y = np.mgrid[y_int[0]:y_int[1]:300j]
    points = zip(x, y)
    z = [[func([x_s, y_s]) for x_s in x] for y_s in y]
    plt.figure()

    # plot contour
    plt.contour(x, y, z)

    # plot trace
    xs = [point[0] for point in trace]
    ys = [point[1] for point in trace]
    plt.plot(xs, ys, 'k--')

    # plot finish
    plt.plot(xs[-1], ys[-1], 'ro')

    plt.show()
    return

def plotGraph(func, x_int, y_int):
    x, y = np.mgrid[x_int[0]:x_int[1]:100j, y_int[0]:y_int[1]:100j]
    z = func(x, y)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap="plasma")
    plt.show()
    return

def findGlobalMin(func, x_int, y_int):
    # init intervals like in intvalpy
    a = [x_int[0], y_int[0]]
    b = [x_int[1], y_int[1]]
    X = iv.Interval(a, b)
    
    # find mins
    Y = X
    y = func(Y).a
    L = [[Y, y]]
    trace = []

    while (func(Y).wid >= EPS):
        l = 0
        maxWid = Y[l].wid
        for i in range(2):
            if i != l and Y[i].wid > maxWid:
                maxWid = Y[i].wid
                l = i
        
        Y1, Y2 = copy.deepcopy(Y), copy.deepcopy(Y)
        Y1[l] = iv.Interval(Y[l].a, Y[l].mid)
        Y2[l] = iv.Interval(Y[l].mid, Y[l].b)

        v1, v2 = func(Y1).a, func(Y2).a

        L = L[1:]
        L.append([Y2, v2])
        L.append([Y1, v1])
        L.sort(key=lambda tup : tup[1])
        # prepaire for next iteration
        Y, y = L[0][0], L[0][1]
        trace.append(Y.mid)
    return trace, y

if __name__ == '__main__':
    # one global min func params
    X_INT_1 = [-10, 10]
    Y_INT_1 = [-10, 10]
    func_1 = booth
    func_1_1 = booth_1

    # more than one global min func param
    X_INT_2 = [-5, 5]
    Y_INT_2 = [-5, 5]
    func_2 = himmelblausFunc
    func_2_1 = himmelblausFunc_1

    # one global min func
    plotGraph(func_1_1, X_INT_1, Y_INT_1)
    trace_1, ans = findGlobalMin(func_1, X_INT_1, Y_INT_1)
    print(trace_1[-1], ans)
    plotTrace(func_1, trace_1, X_INT_1, Y_INT_1)

    # more than one global min func
    plotGraph(func_2_1, X_INT_2, Y_INT_2)
    trace_2, ans = findGlobalMin(func_2, X_INT_2, Y_INT_2)
    plotTrace(func_2, trace_2, X_INT_2, Y_INT_2)
    print(trace_2[-1], ans)
