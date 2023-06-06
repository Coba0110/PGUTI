import tkinter as tk
from tkinter import messagebox

def calculate_y(x):
    # Здесь должна быть логика расчета значения у(х) в соответствии с выбранным вариантом
    # В данном примере просто возвращаем куб x
    return x ** 3

def calculate_criteria(y_values):
    # Расчет критериев
    max_value = max(y_values)
    min_value = min(y_values)
    sum_all = sum(y_values)
    product_all = 1
    sum_negative = 0
    product_negative = 1
    sum_positive = 0
    product_positive = 1

    for y in y_values:
        product_all *= y
        if y < 0:
            sum_negative += y
            product_negative *= y
        elif y > 0:
            sum_positive += y
            product_positive *= y

    return {
        "Максимальный элемент": max_value,
        "Минимальный элемент": min_value,
        "Сумма всех элементов": sum_all,
        "Произведение всех элементов": product_all,
        "Сумма отрицательных элементов": sum_negative,
        "Произведение отрицательных элементов": product_negative,
        "Сумма положительных элементов": sum_positive,
        "Произведение положительных элементов": product_positive
    }

def show_positive_elements(y_values):
    positive_elements = [y for y in y_values if y > 0]
    if positive_elements:
        messagebox.showinfo("Положительные элементы", ", ".join(str(y) for y in positive_elements))
    else:
        messagebox.showinfo("Положительные элементы", "Положительные элементы отсутствуют")

def show_negative_elements(y_values):
    negative_elements = [y for y in y_values if y < 0]
    if negative_elements:
        messagebox.showinfo("Отрицательные элементы", ", ".join(str(y) for y in negative_elements))
    else:
        messagebox.showinfo("Отрицательные элементы", "Отрицательные элементы отсутствуют")

def exit_program():
    choice = messagebox.askquestion("Выход", "Вы действительно хотите выйти из программы?")
    if choice == "yes":
        window.destroy()

def calculate_y_and_criteria():
    A = entry_A.get()
    if not A:
        messagebox.showwarning("Ошибка", "Введите значение параметра A")
        return

    try:
        A = float(A)
    except ValueError:
        messagebox.showwarning("Ошибка", "Некорректное значение параметра A")
        return

    M = 5  # Пример значения M
    N = 3  # Пример значения N
    beta = abs(M - N)
    # Здесь должна быть логика выбора компонента ввода A из таблицы 2 в соответствии с beta
    # В данном примере просто выводим A на консоль
    print("Значение A:", A)

    y = calculate_y(A)
    y_values.append(y)
    listbox_values.insert(tk.END, f"x={A}, y={y}")

    criteria = calculate_criteria(y_values)
    messagebox.showinfo("Рассчитанные критерии", "\n".join(f"{key}: {value}" for key, value in criteria.items()))

def show_menu(event):
    popup_menu.post(event.x_root, event.y_root)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

window = tk.Tk()

menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Выход", command=exit_program)
menubar.add_cascade(label="Файл", menu=file_menu)
window.config(menu=menubar)

context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="Выход", command=exit_program)
context_menu.add_command(label="Расчет у(x) и критериев", command=calculate_y_and_criteria)
context_menu.add_command(label="Максимальный элемент", command=lambda: messagebox.showinfo("Критерий", str(criteria["Максимальный элемент"])))
context_menu.add_command(label="Минимальный элемент", command=lambda: messagebox.showinfo("Критерий", str(criteria["Минимальный элемент"])))
context_menu.add_command(label="Сумма всех элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма всех элементов"])))
context_menu.add_command(label="Произведение всех элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение всех элементов"])))
context_menu.add_command(label="Сумма отрицательных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма отрицательных элементов"])))
context_menu.add_command(label="Произведение отрицательных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение отрицательных элементов"])))
context_menu.add_command(label="Сумма положительных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма положительных элементов"])))
context_menu.add_command(label="Произведение положительных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение положительных элементов"])))
context_menu.add_command(label="Положительные элементы", command=lambda: show_positive_elements(y_values))
context_menu.add_command(label="Отрицательные элементы", command=lambda: show_negative_elements(y_values))

window.bind("<Button-3>", show_context_menu)

form = tk.Frame(window)
form.pack()

label_A = tk.Label(form, text="Введите значение параметра A:")
label_A.pack()

entry_A = tk.Entry(form)
entry_A.pack()

calculate_button = tk.Button(form, text="Рассчитать у(x) и критерии", command=calculate_y_and_criteria)
calculate_button.pack()

listbox_values = tk.Listbox(form)
listbox_values.pack()

scrollbar = tk.Scrollbar(form, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_values.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_values.yview)

y_values = []
criteria = {}

popup_menu = tk.Menu(window, tearoff=0)
popup_menu.add_command(label="Выход", command=exit_program)
popup_menu.add_command(label="Расчет у(x) и критериев", command=calculate_y_and_criteria)
popup_menu.add_command(label="Максимальный элемент", command=lambda: messagebox.showinfo("Критерий", str(criteria["Максимальный элемент"])))
popup_menu.add_command(label="Минимальный элемент", command=lambda: messagebox.showinfo("Критерий", str(criteria["Минимальный элемент"])))
popup_menu.add_command(label="Сумма всех элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма всех элементов"])))
popup_menu.add_command(label="Произведение всех элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение всех элементов"])))
popup_menu.add_command(label="Сумма отрицательных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма отрицательных элементов"])))
popup_menu.add_command(label="Произведение отрицательных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение отрицательных элементов"])))
popup_menu.add_command(label="Сумма положительных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Сумма положительных элементов"])))
popup_menu.add_command(label="Произведение положительных элементов", command=lambda: messagebox.showinfo("Критерий", str(criteria["Произведение положительных элементов"])))
popup_menu.add_command(label="Положительные элементы", command=lambda: show_positive_elements(y_values))
popup_menu.add_command(label="Отрицательные элементы", command=lambda: show_negative_elements(y_values))

window.bind("<Button-3>", show_context_menu)

window.mainloop()
