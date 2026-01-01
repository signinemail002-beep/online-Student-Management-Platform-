import tkinter as tk
from tkinter import messagebox, simpledialog
from Manager import AuthSystem  
from Manager import StudentManager
from Manager import Student
from PIL import Image, ImageTk


# ===== USE YOUR BACKEND CLASSES =====
# (AuthSystem, Student, StudentManager must already exist)

auth = AuthSystem()
manager = StudentManager()


# ================= LOGIN WINDOW =================


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("340x300")
        self.root.configure(bg="#f0f4f8")

        # ===== Title =====
        tk.Label(
            root,
            text="Student Management Login",
            font=("Arial", 16, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        ).pack(pady=15)

        # ===== Username =====
        tk.Label(
            root,
            text="Username",
            bg="#f0f4f8",
            fg="#555",
            font=("Arial", 11)
        ).pack(pady=(10, 3))

        self.username_entry = tk.Entry(
            root,
            font=("Arial", 12),
            width=24,
            relief="solid",
            bd=1
        )
        self.username_entry.pack()

        # ===== Password =====
        tk.Label(
            root,
            text="Password",
            bg="#f0f4f8",
            fg="#555",
            font=("Arial", 11)
        ).pack(pady=(12, 3))

        self.password_entry = tk.Entry(
            root,
            show="*",
            font=("Arial", 12),
            width=24,
            relief="solid",
            bd=1
        )
        self.password_entry.pack()

        # ===== Buttons Frame =====
        btn_frame = tk.Frame(root, bg="#f0f4f8")
        btn_frame.pack(pady=25)

        # ===== Login Button =====
        tk.Button(
            btn_frame,
            text="Login",
            command=self.login,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            pady=6,
            relief="flat",
            cursor="hand2"
        ).grid(row=0, column=0, padx=8)

        # ===== Exit Button =====
        tk.Button(
            btn_frame,
            text="Exit",
            command=root.destroy,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            pady=6,
            relief="flat",
            cursor="hand2"
        ).grid(row=0, column=1, padx=8)

    def login(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()

        if user == auth.username and pwd == auth.password:
            self.root.destroy()
            open_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")



# ================= MAIN MENU WINDOW =================

def open_main_menu():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("420x600")
    root.configure(bg="#f5f6fa")

    # ==== Title ====
    tk.Label(
        root,
        text="Student Management System",
        font=("Arial", 16, "bold"),
        bg="#f5f6fa",
        fg="#2c3e50"
    ).pack(pady=15)

    #==== Image ====
    img = Image.open("student.png")
    img = img.resize((180, 180))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo, bg="#f5f6fa")
    img_label.image = photo
    img_label.pack(pady=5)
    # ===== Buttons Style =====
    button_style = {
        "font": ("Arial", 11, "bold"),
        "fg": "white",
        "width": 28,
        "relief": "flat",
        "cursor": "hand2",
        "pady": 6
    }

    tk.Button(
        root, text="Add Student",
        bg="#3498db",
        activebackground="#2980b9",
        command=add_student,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Remove Student",
        bg="#e74c3c",
        activebackground="#c0392b",
        command=remove_student,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Update Student",
        bg="#2196F3",
        activebackground="#2196F3",
       command=update_student,
        **button_style
    ).pack(pady=4)


    tk.Button(
        root, text="View All Students",
        bg="#2ecc71",
        activebackground="#27ae60",
        command=view_students,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Search Student",
        bg="#9b59b6",
        activebackground="#8e44ad",
        command=search_student,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Add Grade",
        bg="#f39c12",
        activebackground="#e67e22",
        command=add_grade,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Student Average",
        bg="#1abc9c",
        activebackground="#16a085",
        command=show_average,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Save Data",
        bg="#34495e",
        activebackground="#2c3e50",
        command=save_data,
        **button_style
    ).pack(pady=4)

    tk.Button(
        root, text="Exit",
        bg="#FF004C",
        activebackground="#FF0000",
        command=root.destroy,
        **button_style
    ).pack(pady=10)

    root.mainloop()

BTN_BG = "#4CAF50"          # Green
BTN_FG = "white"
BTN_FONT = ("Arial", 10, "bold")
LABEL_FONT = ("Arial", 10)
ENTRY_FONT = ("Arial", 10)
WIN_BG = "#f5f5f5"


def add_student():
    add_win = tk.Toplevel()
    add_win.title("Add Student")
    add_win.geometry("320x320")
    add_win.configure(bg=WIN_BG)

    tk.Label(add_win, text="Add New Student", font=("Arial", 12, "bold"),
             bg=WIN_BG).pack(pady=10)

    # === Student ID ===
    tk.Label(add_win, text="Student ID", bg=WIN_BG, font=LABEL_FONT).pack()
    sid_entry = tk.Entry(add_win, font=ENTRY_FONT)
    sid_entry.pack(pady=5)

    # === Name ===
    tk.Label(add_win, text="Name", bg=WIN_BG, font=LABEL_FONT).pack()
    name_entry = tk.Entry(add_win, font=ENTRY_FONT)
    name_entry.pack(pady=5)

    # === Age ===
    tk.Label(add_win, text="Age", bg=WIN_BG, font=LABEL_FONT).pack()
    age_entry = tk.Entry(add_win, font=ENTRY_FONT)
    age_entry.pack(pady=5)

    # === Major ===
    tk.Label(add_win, text="Major", bg=WIN_BG, font=LABEL_FONT).pack()
    major_entry = tk.Entry(add_win, font=ENTRY_FONT)
    major_entry.pack(pady=5)

    def save_student():
        sid = sid_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        major = major_entry.get()

        if not sid or not name or not age or not major:
            messagebox.showerror("Error", "All fields are required")
            return

        if sid in manager.students:
            messagebox.showerror("Error", "Student already exists")
            return

        try:
            student = Student(sid, name, int(age), major)
            manager.students[sid] = student
            messagebox.showinfo("Success", "Student added successfully")
            add_win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Age must be a number")

    tk.Button(
        add_win,
        text="Save Student",
        command=save_student,
        bg=BTN_BG,
        fg=BTN_FG,
        font=BTN_FONT,
        width=20
    ).pack(pady=15)

    



# ================= FUNCTIONS =================



def remove_student():
    win = tk.Toplevel()
    win.title("Remove Student")
    win.geometry("300x180")
    win.configure(bg="#f4f6f7")

    tk.Label(
        win,
        text="Remove Student",
        font=("Arial", 14, "bold"),
        bg="#f4f6f7",
        fg="#c0392b"
    ).pack(pady=10)

    tk.Label(
        win,
        text="Student ID:",
        bg="#f4f6f7",
        font=("Arial", 11)
    ).pack(pady=5)

    sid_entry = tk.Entry(win, width=25, font=("Arial", 11))
    sid_entry.pack(pady=5)

    def confirm_remove():
        sid = sid_entry.get()

        if not sid:
            messagebox.showerror("Error", "Please enter Student ID")
            return

        result = manager.remove_student(sid)

        if result:
            messagebox.showinfo("Success", "Student removed successfully")
            win.destroy()
        else:
            messagebox.showerror("Error", "Student not found")

    tk.Button(
        win,
        text="Remove",
        bg="#e74c3c",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        width=15,
        command=confirm_remove
    ).pack(pady=15)

    tk.Button(
        win,
        text="Cancel",
        bg="#95a5a6",
        fg="white",
        font=("Arial", 10),
        relief="flat",
        width=15,
        command=win.destroy
    ).pack()



def update_student():
    win = tk.Toplevel()
    win.title("Update Student")
    win.geometry("500x500")
    win.configure(bg="#f4f6f7")

    win.configure(bg="#f0f4f8")

   # ===== Title =====
    tk.Label(
      win,
      text="Update Student Information",
      font=("Arial", 18, "bold"),
      bg="#f0f4f8",
      fg="#2c5042"
    ).pack(pady=15)

   # ===== Card Frame =====
    card = tk.Frame(
     win,
     bg="white",
     bd=1,
     relief="solid"
    )
    card.pack(padx=25, pady=10, fill="both", expand=True)

    # ===== Helper function for rows =====
    def form_row(parent, label_text, row):
     tk.Label(
         parent,
         text=label_text,
         bg="white",
         fg="#34495e",
         font=("Arial", 11),
         anchor="w"
        ).grid(row=row, column=0, padx=15, pady=10, sticky="w")

     entry = tk.Entry(
         parent,
         width=25,
         font=("Arial", 11),
         relief="solid",
         bd=1
        )
     entry.grid(row=row, column=1, padx=15, pady=10)
     return entry

   # ===== Input Fields =====
    sid_entry = form_row(card, "Student ID *", 0)
    name_entry = form_row(card, "New Name (optional)", 1)
    age_entry = form_row(card, "New Age (optional)", 2)
    major_entry = form_row(card, "New Major (optional)", 3)

  # ===== Buttons Frame =====
    btn_frame = tk.Frame(win, bg="#f0f4f8")
    btn_frame.pack(pady=15)

    tk.Button(
     btn_frame,
     text="Update",
     font=("Arial", 11, "bold"),
     bg="#3498db",
     fg="white",
     padx=20,
     pady=6,
     relief="flat",
     cursor="hand2",
     command=update_student  # <-- your update function
    ).grid(row=0, column=0, padx=10)

    tk.Button(
     btn_frame,
     text="Cancel",
     font=("Arial", 11),
     bg="#e74c3c",
     fg="white",
     padx=20,
     pady=6,
     relief="flat",
     cursor="hand2",
     command=win.destroy
    ).grid(row=0, column=1, padx=10)

   
    def save_update():
        sid = sid_entry.get().strip()
        name = name_entry.get()
        age = age_entry.get()
        major = major_entry.get()

        if not sid:
            messagebox.showerror("Error", "Student ID is required")
            return

        success = manager.update_student(
            sid,
            name=name,
            age=age,
            major=major
        )

        if success:
            messagebox.showinfo("Success", "Student updated successfully")
            win.destroy()
        else:
            messagebox.showerror("Error", "Student not found")

    

def view_students():
    if not manager.students:
        messagebox.showinfo("Info", "No students found")
        return

    win = tk.Toplevel()
    win.title("All Students")
    win.geometry("600x350")
    win.configure(bg="#f2f2f2")

    # ===== Title =====
    title = tk.Label(
        win,
        text="All Students",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#333"
    )
    title.pack(pady=10)

    # ===== Table Frame =====
    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=10, pady=5)

    # ===== Scrollbar =====
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # ===== Treeview Table =====
    columns = ("ID", "Name", "Age", "Major")

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings",
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(command=tree.yview)

    # ===== Table Headings =====
    tree.heading("ID", text="Student ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Major", text="Major")

    # ===== Column Widths =====
    tree.column("ID", width=100, anchor="center")
    tree.column("Name", width=150)
    tree.column("Age", width=80, anchor="center")
    tree.column("Major", width=150)

    tree.pack(fill="both", expand=True)

    # ===== Insert Student Data =====
    for s in manager.students.values():
        tree.insert(
            "",
            tk.END,
            values=(s.sid, s.name, s.age, s.major)
        )

    # ===== Style (Modern Look) =====
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        background="white",
        foreground="black",
        rowheight=25,
        fieldbackground="white"
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 10, "bold"),
        background="#4CAF50",
        foreground="white"
    )

    style.map(
        "Treeview",
        background=[("selected", "#2196F3")]
    )
    # ===== Close Button =====
    tk.Button(
        win,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="#e74c3c",
        fg="white",
        activebackground="#c0392b",
        width=15,
        command=win.destroy
    ).pack(pady=10)




def search_student():
    win = tk.Toplevel()
    win.title("Search Student")
    win.geometry("700x500")
    win.minsize(500, 350)
    win.configure(bg="#f4f6f7")
    win.resizable(True, True)

    # ===== Title =====
    tk.Label(
        win,
        text="Search Student",
        font=("Arial", 18, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=10)
    # ===== Input Card =====
    input_frame = tk.Frame(
      win,
      bg="white",
      bd=1,
      relief="solid"
    )
    input_frame.pack(pady=25, padx=25, fill="x")

   # Label
    tk.Label(
      input_frame,
      text="Student ID",
      font=("Segoe UI", 12, "bold"),
      bg="white",
      fg="#2c3e50"
    ).pack(anchor="w", padx=15, pady=(5))

    # Entry (Bigger & cleaner)
    sid_entry = tk.Entry(
       input_frame,
       font=("Segoe UI", 14),
       width=28,
       bd=1,
       relief="solid"
    )
    sid_entry.pack(padx=15, pady=(0, 15), ipady=6)

   # Auto focus
    sid_entry.focus()
    sid_entry.insert(0, "Enter student ID")
    sid_entry.config(fg="#999")

    def on_focus_in(event):
      if sid_entry.get() == "Enter student ID":
         sid_entry.delete(0, tk.END)
         sid_entry.config(fg="#000")

    def on_focus_out(event):
      if not sid_entry.get():
         sid_entry.insert(0, "Enter student ID")
         sid_entry.config(fg="#999")

    sid_entry.bind("<FocusIn>", on_focus_in)
    sid_entry.bind("<FocusOut>", on_focus_out)


    

    # ===== Search Logic =====
    def search():
        sid = sid_entry.get().strip()

        if sid not in manager.students:
            messagebox.showerror("Error", "Student not found")
            return

        s = manager.students[sid]

        # ===== Result Window =====
        result_win = tk.Toplevel()
        result_win.title("Student Details")
        result_win.geometry("700x500")
        result_win.minsize(500, 350)
        result_win.configure(bg="#f2f4f8")
        result_win.resizable(True, True)

        # ===== Header =====
        tk.Label(
            result_win,
            text="Student Information",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 14, "bold"),
            pady=10
        ).pack(fill="x")

        # ===== Card =====
        card = tk.Frame(
            result_win,
            bg="white",
            bd=1,
            relief="solid"
        )
        card.pack(padx=20, pady=20, fill="both", expand=True)

        # ===== Row Function =====
        def info_row(label, value):
            row = tk.Frame(card, bg="white")
            row.pack(fill="x", padx=15, pady=6)

            tk.Label(
                row,
                text=label,
                width=10,
                anchor="w",
                bg="white",
                fg="#555",
                font=("Arial", 10, "bold")
            ).pack(side="left")

            tk.Label(
                row,
                text=value,
                anchor="w",
                bg="white",
                fg="#000",
                font=("Arial", 10)
            ).pack(side="left", fill="x")

            tk.Frame(card, height=1, bg="#e0e0e0").pack(fill="x", padx=10)

        # ===== Student Data =====
        info_row("ID", s.sid)
        info_row("Name", s.name)
        info_row("Age", str(s.age))
        info_row("Major", s.major)

        # ===== Close Button (Result Window) =====
        tk.Button(
            result_win,
            text="Close",
            command=result_win.destroy,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=6,
            relief="flat",
            cursor="hand2"
        ).pack(pady=10)

    # ===== Buttons Frame =====
    btn_frame = tk.Frame(win, bg="#f4f6f7")
    btn_frame.pack(pady=15)

    # ===== Search Button =====
    tk.Button(
        btn_frame,
        text="Search",
        command=search,
        bg="#3498db",
        fg="white",
        font=("Arial", 11, "bold"),
        width=12,
        relief="flat",
        cursor="hand2"
    ).grid(row=0, column=0, padx=5)

    # ===== Close Button (Search Window) =====
    tk.Button(
        btn_frame,
        text="Close",
        command=win.destroy,
        bg="#F44336",
        fg="white",
        font=("Arial", 11, "bold"),
        width=12,
        relief="flat",
        cursor="hand2"
    ).grid(row=0, column=1, padx=5)




def add_grade():
    win = tk.Toplevel()
    win.title("Add Grade")
    win.geometry("350x350")
    win.configure(bg=WIN_BG)

    FONT_LABEL = ("Arial", 12, "bold")
    FONT_ENTRY = ("Arial", 14)

    # ===== Input Frame =====
    form_frame = tk.Frame(win, bg=WIN_BG)
    form_frame.pack(pady=20)

    # ===== Student ID =====
    tk.Label(
      form_frame,
      text="Student ID",
      bg=WIN_BG,
      font=FONT_LABEL
    ).grid(row=0, column=0, sticky="w", pady=8)

    sid_entry = tk.Entry(
      form_frame,
      font=FONT_ENTRY,
      width=25,
      bd=2,
      relief="groove"
    )
    sid_entry.grid(row=1, column=0, pady=5, ipady=6)

    # ===== Grade =====
    tk.Label(
      form_frame,
      text="Grade (0–100)",
      bg=WIN_BG,
      font=FONT_LABEL
    ).grid(row=2, column=0, sticky="w", pady=8)

    grade_entry = tk.Entry(
      form_frame,
      font=FONT_ENTRY,
      width=25,
      bd=2,
      relief="groove"
    )
    grade_entry.grid(row=3, column=0, pady=5, ipady=6)

    

    def save_grade():
        sid = sid_entry.get()
        try:
            grade = int(grade_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Grade must be a number")
            return

        if sid not in manager.students:
            messagebox.showerror("Error", "Student not found")
            return

        if manager.students[sid].add_grade(grade):
            messagebox.showinfo("Success", "Grade added successfully")
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid grade")
    
     # ===== Buttons Frame =====
    btn_frame = tk.Frame(win, bg="#f4f6f7")
    btn_frame.pack(pady=15)

    tk.Button(
      btn_frame,
      text="Add Grade",
      command=save_grade,
      bg="#2196F3",
      fg="white",
      font=BTN_FONT,
      width=16,
      relief="flat",
      cursor="hand2"
    ).pack(side="left", padx=15)

    tk.Button(
     btn_frame,
     text="Cancel",
     command=win.destroy,
     bg="#F44336",
     fg="white",
     font=BTN_FONT,
     width=16,
     relief="flat",
     cursor="hand2"
    ).pack(side="left", padx=15)
    


from tkinter import ttk

def show_average():
    if not manager.students:
        messagebox.showinfo("Info", "No students found")
        return

    win = tk.Toplevel()
    win.title("All Students")
    win.geometry("600x350")
    win.configure(bg="#f0f4f8")

    # ===== Title =====
    tk.Label(
        win,
        text="Student List",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8",
        fg="#333"
    ).pack(pady=10)

    # ===== Table Frame =====
    frame = tk.Frame(win, bg="#f0f4f8")
    frame.pack(fill="both", expand=True, padx=10)

    columns = ("ID", "Name", "Age", "Major", "Average")

    table = ttk.Treeview(frame, columns=columns, show="headings", height=10)

    # ===== Table Headings =====
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)

    # ===== Insert Data =====
    for s in manager.students.values():
        table.insert(
            "",
            "end",
            values=(s.sid, s.name, s.age, s.major, f"{s.average():.2f}")
        )

    table.pack(fill="both", expand=True)

    # ===== Scrollbar =====
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # ===== Close Button =====
    tk.Button(
        win,
        text="Close",
        command=win.destroy,
        bg="#ff6b6b",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=10,
        pady=5
    ).pack(pady=10)


def save_data():
    manager.save_data()
    messagebox.showinfo("Saved", "Data saved successfully")


# ================= START PROGRAM =================
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()