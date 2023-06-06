import tkinter as tk

# Создание окна
window = tk.Tk()
window.title("Движение шарика")
window.geometry("600x600")

# Переменные для координат шарика
x = 300
y = 300

# Переменные для координат линии
line_x = x
line_y = y

# Функция для обновления положения шарика и линии
def update_ball():
    global x, y, line_x, line_y
    
    # Обновление координат шарика
    canvas.coords(ball, x-10, y-10, x+10, y+10)
    
    # Отрисовка линии
    canvas.create_line(line_x, line_y, x, y, fill="red", width=2)
    
    # Обновление координат линии
    line_x = x
    line_y = y
    
    # Вызов функции снова через 100 миллисекунд
    window.after(100, update_ball)

# Функция для движения влево
def move_left_func():
    global x
    x -= 50

# Функция для движения вниз
def move_down_func():
    global y
    y += 50

# Создание холста
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Создание координатной сетки
for i in range(0, 601, 50):
    canvas.create_line(i, 0, i, 600, fill="gray")
    canvas.create_line(0, i, 600, i, fill="gray")

# Создание шарика
ball = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

# Перемещение кнопок в середину окна
button_frame = tk.Frame(window)
button_frame.pack()

# Создание кнопки "Влево"
left_button = tk.Button(button_frame, text="Влево", command=move_left_func)
left_button.pack(side="left")

# Создание кнопки "Вниз"
down_button = tk.Button(button_frame, text="Вниз", command=move_down_func)
down_button.pack(side="left")

# Запуск движения шарика
update_ball()

# Запуск главного цикла
window.mainloop()
