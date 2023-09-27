import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

mpl.use('TkAgg')
fig, ax = plt.subplots()

h = 0.5
x_range = numpy.arange(-2, 3, 0.5)


def f(x, k):
    return (((-2) ** (k + 1)) * math.factorial(k + 1)) / ((x + 2.5) ** (k + 1))


f_table = [sum([f(i, j) for j in range(1, 6)]) for i in x_range]

ax.plot(x_range, f_table)
plt.show()
