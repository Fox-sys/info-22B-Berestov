import numpy as np


def task_1():
    """
    Ввести массив состоящий из 8 двух значных чисел целого типа.
    Получить массив младших разрядов этих чисел.
    :return:
    """
    data = np.array([])
    counter = 0
    while counter < 8:
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Попытка не увенчалась успехом')
            continue
        data = np.append(data, num)
        counter += 1
    print(data % 10)


def task_2():
    """

    :return:
    """
    data = np.array([])
    counter = 0
    while counter < 10:
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Попытка не увенчалась успехом')
            continue
        data = np.append(data, num)
        counter += 1
    mask = 0 < data
    print(np.sum(data[0:np.where(mask == False)[0][0]]))


task_2()
