import tkinter as tk
import os

# Создаём главное окно
root = tk.Tk()
root.title("Валентинка")
root.geometry("350x150")
root.resizable(False, False)

# Применяем кастомную иконку (файл heart.ico)
try:
    root.iconbitmap("heart.ico")
except Exception as e:
    print("Не удалось загрузить иконку:", e)

# Функция для очистки окна
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Диалог 1: "Мы идем на свидание?"
def show_first_dialog():
    clear_window()
    # Надпись по центру
    label = tk.Label(root, text="Мы идем на свидание?", font=("Arial", 12))
    label.pack(expand=True)

    # Рамка для кнопок
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    btn_yes = tk.Button(btn_frame, text="Да", width=10, bg="green", fg="white", command=on_first_yes)
    btn_yes.pack(side="left", padx=5)

    btn_no = tk.Button(btn_frame, text="Нет", width=10, bg="red", fg="white", command=on_first_no)
    btn_no.pack(side="left", padx=5)

# Обработчик для "Да" в диалоге 1
def on_first_yes():
    clear_window()
    label = tk.Label(root, text="А... Об этом я не подумал... Ну ладно, пока!", font=("Arial", 12))
    label.pack(expand=True)
    # Закрытие программы через 3 секунды
    root.after(3000, root.destroy)

# Обработчик для "Нет" в диалоге 1
def on_first_no():
    show_second_dialog()

# Диалог 2: "Ты уверена?"
def show_second_dialog():
    clear_window()
    label = tk.Label(root, text="Ты уверена?", font=("Arial", 12))
    label.pack(expand=True)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    btn_yes = tk.Button(btn_frame, text="Да", width=10, bg="green", fg="white",
                        command=on_second_yes)
    btn_yes.pack(side="left", padx=5)

    btn_no = tk.Button(btn_frame, text="Нет", width=10, bg="red", fg="white",
                       command=on_second_no)
    btn_no.pack(side="left", padx=5)

# Обработчик для "Да" в диалоге 2
def on_second_yes():
    clear_window()
    label = tk.Label(root, text="Очень жаль, папка\nsystem32 будет удалена с Вашего\nкомпьютера...", font=("Arial", 12))
    label.pack(expand=True)
    # Запуск системной команды для выключения компьютера
    # Иногда для выключения ПК могут понадобиться права администратора.
    try:
        os.system("shutdown /s /t 3")
    except Exception as e:
        print("Ошибка при выполнении shutdown:", e)

# Обработчик для "Нет" в диалоге 2
def on_second_no():
    show_first_dialog()

# Запускаем первый диалог
show_first_dialog()

root.mainloop()
