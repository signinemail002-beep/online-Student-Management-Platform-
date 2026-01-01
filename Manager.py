import json
import csv
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
        self.age = int(age)  # Convert to int
        self.major = major
        self.grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:  # Basic validation
            self.grades.append(score)
            return True
        return False

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "grades": self.grades
        }


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
                        s.grades = info["grades"]
                        self.students[sid] = s
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading database: {e}. Starting fresh.")

    def save_data(self):
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        with open(DATABASE, 'w') as f:
            json.dump(data, f, indent=4)

    def add_student(self, sid, name, age, major):
        if sid in self.students:
            print("Student already exists.")
            return False
        
        try:
            age_int = int(age)  # Validate age is a number
            self.students[sid] = Student(sid, name, age_int, major)
            print("Student added successfully.")
            self.save_data()
            return True
        except ValueError:
            print("Age must be a number.")
            return False

    def remove_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("Student removed.")
            self.save_data()
            return True
        else:
            print("Student not found.")
            return False

    def update_student(self, sid, name=None, age=None, major=None):
        if sid not in self.students:
            print("Student not found.")
            return False

        student = self.students[sid]
        if name and name.strip(): 
            student.name = name.strip()
        if age and age.strip():
            try:
                student.age = int(age.strip())
            except ValueError:
                print("Age must be a number. Update skipped.")
        if major and major.strip():
            student.major = major.strip()

        print("Updated successfully.")
        self.save_data()
        return True

    def add_grade(self, sid, grade_str):
        if sid not in self.students:
            print("Student not found.")
            return False
        
        try:
            grade = float(grade_str)
            if self.students[sid].add_grade(grade):
                print("Grade added.")
                self.save_data()
                return True
            else:
                print("Grade must be between 0 and 100.")
                return False
        except ValueError:
            print("Grade must be a number.")
            return False

    def search(self, text):
        result = []
        for s in self.students.values():
            if text.lower() in s.name.lower() or text == s.sid:
                result.append(s)
        return result

    def list_students(self):
        if not self.students:
            print("No students in database.")
            return
        
        print("\nID      | Name                | Age | Major          | Average")
        print("-" * 65)
        for s in self.students.values():
            print(f"{s.sid:<8} | {s.name:<20} | {s.age:<3} | {s.major:<15} | {s.average():.2f}")

    def export_csv(self):
        if not self.students:
            print("No students to export.")
            return
        
        with open("students_export.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Major", "Grades", "Average"])
            for s in self.students.values():
                writer.writerow([s.sid, s.name, s.age, s.major, 
                               ', '.join(map(str, s.grades)) if s.grades else '', 
                               s.average()])
        print(f"Exported {len(self.students)} students to students_export.csv")


def get_input(prompt, required=True):
    """Helper function to get validated input"""
    while True:
        value = input(prompt).strip()
        if not value and required:
            print("This field is required.")
        else:
            return value


def main():
    auth = AuthSystem()
    if not auth.login():
        print("Access denied.")
        return

    Manager = StudentManager()
    print("\n" + "="*40)
    print("Student Management System v1.0")
    print("="*40)

    while True:
        print("""
        ===== MAIN MENU =====
        1. Add Student
        2. Remove Student
        3. Update Student
        4. Add Grade
        5. Search Student
        6. List All Students
        7. Export to CSV
        0. Exit
        """)
        
        choice = get_input("Choose option (0-7): ")
        
        if choice == "1":
            print("\n--- Add New Student ---")
            sid = get_input("Student ID: ")
            name = get_input("Name: ")
            age = get_input("Age: ")
            major = get_input("Major: ")
            Manager.add_student(sid, name, age, major)
            
        elif choice == "2":
            print("\n--- Remove Student ---")
            sid = get_input("Student ID to remove: ")
            Manager.remove_student(sid)
            
        elif choice == "3":
            print("\n--- Update Student ---")
            sid = get_input("Student ID to update: ")
            name = get_input("New Name (enter to skip): ", required=False)
            age = get_input("New Age (enter to skip): ", required=False)
            major = get_input("New Major (enter to skip): ", required=False)
            Manager.update_student(sid, name, age, major)
            
        elif choice == "4":
            print("\n--- Add Grade ---")
            sid = get_input("Student ID: ")
            grade = get_input("Grade (0-100): ")
            Manager.add_grade(sid, grade)
            
        elif choice == "5":
            print("\n--- Search Student ---")
            text = get_input("Search by Name or ID: ")
            results = Manager.search(text)
            if results:
                print(f"\nFound {len(results)} student(s):")
                for r in results:
                    print(f"  {r.sid}: {r.name}, {r.age}, {r.major}, "
                          f"Grades: {r.grades}, Avg: {r.average():.2f}")
            else:
                print("No students found.")
                
        elif choice == "6":
            print("\n--- All Students ---")
            Manager.list_students()
            
        elif choice == "7":
            print("\n--- Export to CSV ---")
            Manager.export_csv()
            
        elif choice == "0":
            print("\nGoodbye!")
            break
            
        else:
            print("Invalid option. Please enter 0-7.")


if __name__ == "__main__":
    main()