
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange,meshgrid, exp

def f0(x):
    return exp(x[0])*(4 * x[0]*x[0] + 2 * x[1]*x[1] + 4 * x[0] * x[1] + 2 * x[1] + 1)

def f1(x):
    return 4 * x[0]*x[0] + 2 * x[1]*x[1] + 4 * x[0] * x[1] + 2 * x[1] + 1


x = arange(-20,20,.1)
y = arange(-20,20,.1)
X,Y = meshgrid(x, y) # grid of point
Z = f0([X, Y]) # evaluate objactive function
#Z = f1([X, Y]) # evaluate only polynomial part

ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap="jet")
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
plt.savefig("polyexp.png")