import math
import tkinter as tk
from tkinter import messagebox

def calculate_function(x, A):
    if A == 2:
        return math.cos(x)**2 + A
    elif A == -1:
        return (x**3 - A) / 10
    elif A == 5:
        return math.sqrt(x + A)

def calculate_criteria(y_values):
    if len(y_values) == 0:
        messagebox.showinfo("Ошибка", "Рассчитайте функцию у(х) сначала.")
        return

    max_value = max(y_values)
    min_value = min(y_values)
    sum_all = sum(y_values)
    product_all = math.prod(y_values)
    sum_negative = sum([value for value in y_values if value < 0])
    product_negative = math.prod([value for value in y_values if value < 0])
    sum_positive = sum([value for value in y_values if value > 0])
    product_positive = math.prod([value for value in y_values if value > 0])

    messagebox.showinfo("Критерии",
        f"Максимальный элемент: {max_value}\n"
        f"Минимальный элемент: {min_value}\n"
        f"Сумма всех элементов: {sum_all}\n"
        f"Произведение всех элементов: {product_all}\n"
        f"Сумма отрицательных элементов: {sum_negative}\n"
        f"Произведение отрицательных элементов: {product_negative}\n"
        f"Сумма положительных элементов: {sum_positive}\n"
        f"Произведение положительных элементов: {product_positive}"
    )

    positive_values = [value for value in y_values if value > 0]
    negative_values = [value for value in y_values if value < 0]

    messagebox.showinfo("Положительные элементы", str(positive_values))
    messagebox.showinfo("Отрицательные элементы", str(negative_values))

def calculate_and_display():
    if not entry_A.get():
        messagebox.showinfo("Ошибка", "Введите значение параметра А.")
        return

    A = float(entry_A.get())
    x_values = [x for x in range(-3, 4)]
    y_values = [calculate_function(x, A) for x in x_values]

    label_y_values["text"] = str(y_values)
    calculate_criteria(y_values)

root = tk.Tk()
root.title("Программа")

label_A = tk.Label(root, text="A:")
label_A.pack()

entry_A = tk.Entry(root)
entry_A.pack()

button_calculate = tk.Button(root, text="Рассчитать", command=calculate_and_display)
button_calculate.pack()

label_y_values = tk.Label(root, text="")
label_y_values.pack()

root.mainloop()
