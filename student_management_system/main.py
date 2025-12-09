from models.manager import SystemManager

def main():
    manager = SystemManager()

    while True:
        print("\nStudent Management System - Menu")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Enroll Student")
        print("4. Add Grade")
        print("5. Mark Attendance (subject-wise)")
        print("6. View Student Report")
        print("7. View All Students")
        print("8. View Enrollments")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("Student ID: ").strip()
            name = input("Full name: ").strip()
            section = input("Section/Batch: ").strip()
            try:
                manager.add_student(sid, name, section)
                print("Student added.")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            code = input("Subject code: ").strip()
            name = input("Subject name: ").strip()
            try:
                credit_hours = int(input("Credit hours (integer): ").strip())
                manager.add_subject(code, name, credit_hours)
                print("Subject added.")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            sid = input("Student ID: ").strip()
            code = input("Subject code: ").strip()
            try:
                manager.enroll_student(sid, code)
                print("Student enrolled in subject.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            sid = input("Student ID: ").strip()
            code = input("Subject code: ").strip()
            grade = input("Grade (numeric): ").strip()
            try:
                grade_val = float(grade)
                manager.add_grade(sid, code, grade_val)
                print("Grade added.")
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            subject_code = input("Subject code: ").strip()
            try:
                manager.mark_attendance_for_subject(subject_code)
            except Exception as e:
                print("Error:", e)

        elif choice == "6":
            sid = input("Student ID: ").strip()
            try:
                manager.view_student_report(sid)
            except Exception as e:
                print("Error:", e)

        elif choice == "7":
            manager.view_all_students()

        elif choice == "8":
            print("\n----- Enrollments -----")
            for sid, sc in manager.enrollments:
                print(f"{sid} | {sc}")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

