import math

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy
import scipy

mpl.use('TkAgg')
fig, ax = plt.subplots()


def task_1():
    """
    Составить схему алгоритма и написать программу вычисления таблицы значений для заданной функции и построить график
    """
    h = 0.5
    x_range = numpy.arange(-2, 3, h)
    k_range = numpy.arange(1, 6)

    def f(x, k):
        return x * k
    #
    k_upper = numpy.sum(((-2) ** k_range) * scipy.special.factorial(k_range+1))
    x_lower = x_range + 2.5
    k_lower = k_range + 1
    f_table = k_upper / numpy.array([x_lower ** i for i in k_lower]).sum(axis=0)

    ax.plot(x_range, f_table)
    plt.show()


def task_2():
    """
    Составить схему алгоритма и написать программу вычисления таблицы значений для заданной функции и построить график
    """
    h = 0.25
    x_range = numpy.arange(-5, 5, h)
    k_range = numpy.arange(1, 6)
    pi_range = numpy.pi ** (x_range * 3.5)
    upper_range = numpy.sum(numpy.array([x_range ** i for i in k_range]), axis=0)
    f_table = numpy.append(upper_range[x_range > 0], pi_range[x_range <= 0])
    ax.plot(x_range, f_table)
    plt.show()


task_1()
