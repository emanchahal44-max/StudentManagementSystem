import os
from models.student import Student
from models.subject import Subject
from models.record import Record

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
SUBJECTS_FILE = os.path.join(DATA_DIR, "subjects.txt")
ENROLLMENTS_FILE = os.path.join(DATA_DIR, "enrollments.txt")
RECORDS_FILE = os.path.join(DATA_DIR, "records.txt")


class SystemManager:
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.enrollments = set()
        self.records = {}
        self._ensure_data_dir()
        self.load_all()

    def _ensure_data_dir(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        for file in [STUDENTS_FILE, SUBJECTS_FILE, ENROLLMENTS_FILE, RECORDS_FILE]:
            if not os.path.exists(file):
                open(file, "w", encoding="utf-8").close()

    def load_all(self):
        self.load_students()
        self.load_subjects()
        self.load_enrollments()
        self.load_records()
        for sid, sc in self.enrollments:
            if (sid, sc) not in self.records:
                self.records[(sid, sc)] = Record(sid, sc)

    def load_students(self):
        self.students.clear()
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        student = Student.from_line(line)
                        self.students[student.student_id] = student
                    except:
                        pass

    def load_subjects(self):
        self.subjects.clear()
        with open(SUBJECTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        subject = Subject.from_line(line)
                        self.subjects[subject.code] = subject
                    except:
                        pass

    def load_enrollments(self):
        self.enrollments.clear()
        with open(ENROLLMENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) == 2:
                        self.enrollments.add((parts[0], parts[1]))

    def load_records(self):
        self.records.clear()
        with open(RECORDS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        record = Record.from_line(line)
                        self.records[(record.student_id, record.subject_code)] = record
                    except:
                        pass

    def save_students(self):
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            for student in self.students.values():
                f.write(student.to_line() + "\n")

    def save_subjects(self):
        with open(SUBJECTS_FILE, "w", encoding="utf-8") as f:
            for subject in self.subjects.values():
                f.write(subject.to_line() + "\n")

    def save_enrollments(self):
        with open(ENROLLMENTS_FILE, "w", encoding="utf-8") as f:
            for sid, sc in sorted(self.enrollments):
                f.write(f"{sid} | {sc}\n")

    def save_records(self):
        with open(RECORDS_FILE, "w", encoding="utf-8") as f:
            for key, record in self.records.items():
                f.write(record.to_line() + "\n")

    def add_student(self, student_id, name, section):
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name, section)
        self.save_students()

    def add_subject(self, code, name, credit_hours):
        if code in self.subjects:
            raise ValueError("Subject code already exists.")
        self.subjects[code] = Subject(code, name, credit_hours)
        self.save_subjects()

    def enroll_student(self, student_id, subject_code):
        if student_id not in self.students:
            raise ValueError("Unknown student id")
        if subject_code not in self.subjects:
            raise ValueError("Unknown subject code")
        pair = (student_id, subject_code)
        if pair in self.enrollments:
            raise ValueError("Student already enrolled in this subject")
        self.enrollments.add(pair)
        if pair not in self.records:
            self.records[pair] = Record(student_id, subject_code)
        self.save_enrollments()
        self.save_records()

    def add_grade(self, student_id, subject_code, grade):
        key = (student_id, subject_code)
        if key not in self.records:
            raise ValueError("Student not enrolled in this subject.")
        self.records[key].add_grade(grade)
        self.save_records()

    def mark_attendance_for_subject(self, subject_code):
        print(f"\nMarking attendance for subject: {subject_code}")
        while True:
            sid = input("Enter Student ID to mark attendance (or 'done' to finish): ").strip()
            if sid.lower() == "done":
                break
            if (sid, subject_code) not in self.records:
                print("Student not enrolled in this subject.")
                continue
            while True:
                status = input(f"Is student {sid} present or absent? (P/A): ").strip().upper()
                if status in ["P", "A"]:
                    present = status == "P"
                    break
                else:
                    print("Please enter 'P' for present or 'A' for absent.")
            self.records[(sid, subject_code)].mark_attendance(present)
        self.save_records()
        print("Attendance updated.")

    def view_student_report(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        print("\n----- Student Report -----")
        print(f"ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        enrolled_subjects = [sc for (sid, sc) in self.enrollments if sid == student_id]
        if not enrolled_subjects:
            print("No subjects enrolled.")
            return
        for subject_code in enrolled_subjects:
            subject = self.subjects[subject_code]
            record = self.records[(student_id, subject_code)]
            print(f"\nSubject: {subject.code} - {subject.name}")
            print(f"Grades: {record.grades}")
            avg = record.average_grade()
            if avg is not None:
                print(f"Average Grade: {avg:.2f}")
            print(f"Attendance: {len([a for a in record.attendance if a=='P'])}/{len(record.attendance)}")
            pct = record.attendance_percent()
            if pct is not None:
                print(f"Attendance %: {pct:.1f}%")

    def view_all_students(self):
        print("\n----- All Students -----")
        for s in self.students.values():
            print(f"{s.student_id} | {s.name} | {s.section}")


