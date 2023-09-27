import numpy as np


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
print(np.array(list(map(lambda x: x % 10, data))))
