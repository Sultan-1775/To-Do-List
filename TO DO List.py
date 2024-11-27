import tkinter as tk
from tkinter import messagebox

# Задачи
tasks = []

# Функции для добавления и удаления задач
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ошибка", "Введите задачу!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")

# Функция для переключения темы
def toggle_theme():
    if root.cget('bg') == "#f5f5f5":
        root.configure(bg="#333")
        title_label.config(bg="#333", fg="#fff")
        task_entry.config(bg="#444", fg="#fff", insertbackground="white")
        task_listbox.config(bg="#444", fg="#fff")
        add_button.config(bg="#3e8e41")
        remove_button.config(bg="#d32f2f")
    else:
        root.configure(bg="#f5f5f5")
        title_label.config(bg="#f5f5f5", fg="#333")
        task_entry.config(bg="#ffffff", fg="#333", insertbackground="black")
        task_listbox.config(bg="#ffffff", fg="#333")
        add_button.config(bg="#4CAF50")
        remove_button.config(bg="#F44336")

# Создание главного окна
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#f5f5f5")  # Легкий фон

# Верхняя панель
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=10)

title_label = tk.Label(top_frame, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#1e1e1e", fg="#ffffff")
title_label.pack()

# Ввод задачи
task_entry = tk.Entry(root, font=("Helvetica", 16), width=40, bd=2, relief="solid", bg="#f1f1f1", fg="#333", insertbackground="black")
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add task", font=("Helvetica", 16), bg="#4CAF50", fg="white", command=add_task, width=20, height=2)
add_button.pack(pady=5)

# Список задач
task_listbox = tk.Listbox(root, font=("Helvetica", 14), width=35, height=15, bd=4, relief="groove", bg="#ffffff", fg="#333")
task_listbox.pack(pady=10)

# Кнопка удаления
remove_button = tk.Button(root, text="Delete", font=("Helvetica", 16), bg="#F44336", fg="white", command=remove_task, width=20, height=2)
remove_button.pack(pady=5)

# Кнопка для переключения темы
theme_button = tk.Button(root, text="Switch topic", font=("Helvetica", 12), command=toggle_theme)
theme_button.pack(pady=10)

# Запуск приложения
root.mainloop()