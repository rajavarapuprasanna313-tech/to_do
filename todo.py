import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("My To-Do List")
root.geometry("650x650")
root.configure(bg="#EAF4FF")


# ---------------- TASK STORAGE ----------------

tasks = []


# ---------------- FUNCTIONS ----------------

def display_tasks():
    task_list.delete(0, tk.END)

    for number, task in enumerate(tasks, start=1):

        status = "✓" if task["completed"] else "○"

        text = (
            f"{number}. {status} {task['name']}  "
            f"[{task['priority']}]  "
            f"({task['date']})"
        )

        task_list.insert(tk.END, text)

    update_counter()


def add_task(event=None):
    task_name = task_entry.get().strip()
    priority = priority_var.get()

    if task_name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )
        return

    new_task = {
        "name": task_name,
        "priority": priority,
        "completed": False,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    tasks.append(new_task)

    task_entry.delete(0, tk.END)

    display_tasks()


def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete."
        )
        return

    task_number = selected[0]

    tasks.pop(task_number)

    display_tasks()


def complete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )
        return

    task_number = selected[0]

    tasks[task_number]["completed"] = not tasks[task_number]["completed"]

    display_tasks()


def clear_tasks():

    if len(tasks) == 0:
        messagebox.showinfo(
            "Information",
            "There are no tasks to clear."
        )
        return

    answer = messagebox.askyesno(
        "Clear Tasks",
        "Are you sure you want to clear all tasks?"
    )

    if answer:
        tasks.clear()
        display_tasks()


def update_counter():

    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    remaining = total - completed

    counter_label.config(
        text=f"{remaining} Tasks Remaining  •  {completed} Completed"
    )


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 26, "bold"),
    bg="#EAF4FF",
    fg="#243B53"
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Organize your tasks and stay productive",
    font=("Arial", 11),
    bg="#EAF4FF",
    fg="#627D98"
)

subtitle_label.pack()


# ---------------- TASK COUNTER ----------------

counter_label = tk.Label(
    root,
    text="0 Tasks Remaining  •  0 Completed",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF",
    fg="#4A90E2"
)

counter_label.pack(pady=15)


# ---------------- INPUT AREA ----------------

input_frame = tk.Frame(
    root,
    bg="#DCEBFF",
    padx=20,
    pady=20
)

input_frame.pack(
    padx=35,
    fill="x"
)


task_entry = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg="white",
    fg="#243B53",
    bd=0
)

task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)


# Press Enter to add task
task_entry.bind("<Return>", add_task)


# ---------------- PRIORITY ----------------

priority_var = tk.StringVar()
priority_var.set("Medium")

priority_menu = tk.OptionMenu(
    input_frame,
    priority_var,
    "High",
    "Medium",
    "Low"
)

priority_menu.config(
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#243B53",
    bd=0,
    width=8
)

priority_menu.pack(
    side="right",
    padx=(10, 0),
    ipady=5
)


# ---------------- ADD BUTTON ----------------

add_button = tk.Button(
    root,
    text="+  Add Task",
    font=("Arial", 11, "bold"),
    bg="#4A90E2",
    fg="white",
    activebackground="#357ABD",
    activeforeground="white",
    width=20,
    bd=0,
    cursor="hand2",
    command=add_task
)

add_button.pack(
    pady=15,
    ipady=5
)


# ---------------- TASK LIST ----------------

list_frame = tk.Frame(
    root,
    bg="#F0E9FF",
    padx=15,
    pady=15
)

list_frame.pack(
    padx=35,
    pady=5,
    fill="both",
    expand=True
)


task_list = tk.Listbox(
    list_frame,
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#243B53",
    selectbackground="#8E7CC3",
    selectforeground="white",
    bd=0,
    highlightthickness=0
)

task_list.pack(
    fill="both",
    expand=True
)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)

button_frame.pack(pady=20)


complete_button = tk.Button(
    button_frame,
    text="✓ Complete",
    font=("Arial", 10, "bold"),
    bg="#5CB85C",
    fg="white",
    width=13,
    bd=0,
    cursor="hand2",
    command=complete_task
)

complete_button.grid(
    row=0,
    column=0,
    padx=5,
    ipady=5
)


delete_button = tk.Button(
    button_frame,
    text="Delete",
    font=("Arial", 10, "bold"),
    bg="#F28B82",
    fg="white",
    width=13,
    bd=0,
    cursor="hand2",
    command=delete_task
)

delete_button.grid(
    row=0,
    column=1,
    padx=5,
    ipady=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear All",
    font=("Arial", 10, "bold"),
    bg="#9B8AC4",
    fg="white",
    width=13,
    bd=0,
    cursor="hand2",
    command=clear_tasks
)

clear_button.grid(
    row=0,
    column=2,
    padx=5,
    ipady=5
)


# ---------------- START APPLICATION ----------------

root.mainloop()