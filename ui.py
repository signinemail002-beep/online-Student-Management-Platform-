import tkinter as tk
from tkinter import messagebox
from Manager import AuthSystem, StudentManager
from tkinter import ttk


auth = AuthSystem()
manager = StudentManager()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("340x280")
        self.root.configure(bg="#f0f4f8")

        tk.Label(
            root,
            text="Student Management System",
            font=("Arial", 16, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        ).pack(pady=15)

        tk.Label(root, text="Username", bg="#f0f4f8", font=("Arial", 11)).pack(pady=(10, 3))
        self.username_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.username_entry.pack()

        tk.Label(root, text="Password", bg="#f0f4f8", font=("Arial", 11)).pack(pady=(12, 3))
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=24)
        self.password_entry.pack()

        btn_frame = tk.Frame(root, bg="#f0f4f8")
        btn_frame.pack(pady=25)

        tk.Button(
            btn_frame,
            text="Login",
            command=self.login,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            pady=6
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            btn_frame,
            text="Exit",
            command=root.destroy,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            pady=6
        ).grid(row=0, column=1, padx=8)

    def login(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()

        if user == auth.username and pwd == auth.password:
            self.root.destroy()
            open_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


def open_main_menu():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("420x500")
    root.configure(bg="#f5f6fa")

    tk.Label(
        root,
        text="Student Management System",
        font=("Arial", 16, "bold"),
        bg="#f5f6fa",
        fg="#2c3e50"
    ).pack(pady=15)

    button_style = {
        "font": ("Arial", 11, "bold"),
        "fg": "white",
        "width": 28,
        "pady": 6
    }

    tk.Button(
        root, text="Add Student",
        bg="#3498db",
        command=add_student,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="View All Students",
        bg="#2ecc71",
        command=view_students,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Exit",
        bg="#FF004C",
        command=root.destroy,
        **button_style
    ).pack(pady=20)

    root.mainloop()


def add_student():
    win = tk.Toplevel()
    win.title("Add Student")
    win.geometry("320x320")  # 增加高度以容纳按钮
    win.configure(bg="#f5f5f5")

    tk.Label(win, text="Add New Student", font=("Arial", 12, "bold"),
             bg="#f5f5f5").pack(pady=10)

    tk.Label(win, text="Student ID", bg="#f5f5f5", font=("Arial", 10)).pack()
    sid_entry = tk.Entry(win, font=("Arial", 10))
    sid_entry.pack(pady=5)

    tk.Label(win, text="Name", bg="#f5f5f5", font=("Arial", 10)).pack()
    name_entry = tk.Entry(win, font=("Arial", 10))
    name_entry.pack(pady=5)

    tk.Label(win, text="Age", bg="#f5f5f5", font=("Arial", 10)).pack()
    age_entry = tk.Entry(win, font=("Arial", 10))
    age_entry.pack(pady=5)

    tk.Label(win, text="Major", bg="#f5f5f5", font=("Arial", 10)).pack()
    major_entry = tk.Entry(win, font=("Arial", 10))
    major_entry.pack(pady=5)

    def save_student():
        sid = sid_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        major = major_entry.get()

        if not sid or not name or not age or not major:
            messagebox.showerror("Error", "All fields are required")
            return

        # 使用Manager的add_student方法
        success = manager.add_student(sid, name, age, major)
        if success:
            messagebox.showinfo("Success", "Student added successfully")
            win.destroy()
        else:
            # add_student方法内部已经打印了错误信息
            messagebox.showerror("Error", "Failed to add student. Please check console for details.")

    # 保存按钮
    tk.Button(
        win,
        text="Save Student",
        command=save_student,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        pady=8
    ).pack(pady=15)

    # 取消按钮
    tk.Button(
        win,
        text="Cancel",
        command=win.destroy,
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        pady=8
    ).pack(pady=5)


def view_students():
    if not manager.students:
        messagebox.showinfo("Info", "No students found")
        return

    win = tk.Toplevel()
    win.title("All Students")
    win.geometry("600x400")  # 增加高度
    win.configure(bg="#f2f2f2")

    tk.Label(
        win,
        text="All Students",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#333"
    ).pack(pady=10)

    # 创建Frame来容纳表格和滚动条
    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=10, pady=5)

    # 创建滚动条
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # 创建表格
    tree = ttk.Treeview(
        frame,
        columns=("ID", "Name", "Age", "Major"),
        show="headings",
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(command=tree.yview)

    # 设置列标题
    tree.heading("ID", text="Student ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Major", text="Major")

    # 设置列宽
    tree.column("ID", width=100, anchor="center")
    tree.column("Name", width=150)
    tree.column("Age", width=80, anchor="center")
    tree.column("Major", width=200)

    tree.pack(fill="both", expand=True)

    # 添加数据
    for s in manager.students.values():
        tree.insert("", tk.END, values=(s.sid, s.name, s.age, s.major))

    # 关闭按钮
    tk.Button(
        win,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="#e74c3c",
        fg="white",
        width=15,
        command=win.destroy
    ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()