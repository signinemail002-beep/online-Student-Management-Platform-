import json
import os

DATABASE = "students.json"

class AuthSystem:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self):
        print("=== Login Required ===")
        user = input("Username: ")
        pwd = input("Password: ")
        return user == self.username and pwd == self.password


class Student:
    def __init__(self, sid, name, age, major):
        self.sid = sid
        self.name = name
        self.age = int(age)
        self.major = major


class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(DATABASE):
            try:
                with open(DATABASE, 'r') as f:
                    data = json.load(f)
                    for sid, info in data.items():
                        s = Student(info["sid"], info["name"], 
                                   info["age"], info["major"])
                        self.students[sid] = s
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading database: {e}. Starting fresh.")

    def save_data(self):
        data = {}
        for sid, student in self.students.items():
            data[sid] = {
                "sid": student.sid,
                "name": student.name,
                "age": student.age,
                "major": student.major
            }
        with open(DATABASE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def add_student(self, sid, name, age, major):
        if sid in self.students:
            print("Student already exists.")
            return False
        
        try:
            age_int = int(age)
            self.students[sid] = Student(sid, name, age_int, major)
            self.save_data()
            return True
        except ValueError:
            print("Age must be a number.")
            return False

    def list_students(self):
        if not self.students:
            print("No students in database.")
            return
        
        print("\nID      | Name                | Age | Major")
        print("-" * 55)
        for s in self.students.values():
            print(f"{s.sid:<8} | {s.name:<20} | {s.age:<3} | {s.major}")


def main():
    auth = AuthSystem()
    if not auth.login():
        print("Access denied.")
        return

    manager = StudentManager()
    print("\n" + "="*40)
    print("Student Management System v1.0")
    print("="*40)

    while True:
        print("""
        ===== MAIN MENU =====
        1. Add Student
        2. List All Students
        0. Exit
        """)
        
        choice = input("Choose option (0-2): ").strip()
        
        if choice == "1":
            print("\n--- Add New Student ---")
            sid = input("Student ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            major = input("Major: ").strip()
            manager.add_student(sid, name, age, major)
            
        elif choice == "2":
            print("\n--- All Students ---")
            manager.list_students()
            
        elif choice == "0":
            print("\nGoodbye!")
            break
            
        else:
            print("Invalid option. Please enter 0-2.")


if __name__ == "__main__":
    main()