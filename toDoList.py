import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="green4")


root = tk.Tk()
root.title("Список моих задач")
root.configure(background="chartreuse")

label = tk.Label(root, text="Введите вашу задачу:", bg="chartreuse")
label.pack()

entry = tk.Entry(root, width=30, bg="chartreuse2")
entry.pack(pady=10)

task_listBox = tk.Listbox(root, height=10, width=50, bg="GreenYellow", fg="MidnightBlue")
task_listBox.pack(pady=10)

add_btn = tk.Button(root, text="Добавить задачу", command=add_task, bg="chartreuse2", fg="ForestGreen")
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Удалить задачу", command=delete_task, bg="chartreuse2", fg="ForestGreen")
delete_btn.pack(pady=5)

mark_btn = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, bg="chartreuse2", fg="ForestGreen")
mark_btn.pack(pady=5)

root.mainloop()