import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def y(x):
    return x**3 - 2*x**2 + 1

# Задаем параметры
h = 0.02
x_values = np.arange(-10, 10, h)
y_values = [y(x) for x in x_values]

# Построение графика
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x) = x^3 - 2x^2 + 1')
plt.grid(True)
plt.show()

# Вывод таблицы значений
print(' x     |   y(x)')
print('----------------')
for x, y in zip(x_values, y_values):
    print(f'{x:.2f} | {y:.2f}')
