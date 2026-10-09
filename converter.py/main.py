import tkinter as tk
from tkinter import ttk
from CONVERSIONS import CONVERSIONS  


# Создаём окно
root = tk.Tk()
root.title("Мой конвертер")
root.geometry("400x300")
root.resizable(False, False)

# Заголовок
heading = ttk.Label(
    root,
    text="КОНВЕРТЕР ЕДИНИЦ",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15)

# Поле ввода
value_label = ttk.Label(root, text="Введите значение:")
value_label.pack()

value_entry = ttk.Entry(root, font=("Arial", 12), justify="center")
value_entry.pack(pady=8)
value_entry.focus()

# Список конвертаций
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    width=25
)
conversion_box.current(0)
conversion_box.pack(pady=8)

# Функция конвертации
def convert():
    try:
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(
            text="Введите правильное число!",
            foreground="red"
        )
        return

    conversion_name = conversion_box.get()
    converted = CONVERSIONS[conversion_name](value)

    result_label.config(
        text=f"Результат: {converted:.2f}",
        foreground="green"
    )

# Кнопка
convert_button = ttk.Button(
    root,
    text="Конвертировать",
    command=convert
)
convert_button.pack(pady=10)

# Результат
result_label = ttk.Label(
    root,
    text="Результат появится здесь",
    font=("Arial", 11)
)
result_label.pack(pady=5)

# Запуск приложения
root.mainloop()