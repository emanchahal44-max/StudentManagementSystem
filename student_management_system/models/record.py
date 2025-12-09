class Record:
    def __init__(self, student_id, subject_code, grades=None, attendance=None):
        self.student_id = student_id
        self.subject_code = subject_code
        self.grades = grades if grades is not None else []
        self.attendance = attendance if attendance is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)
    
    def mark_attendance(self, present: bool):
        self.attendance.append("P" if present else "A")

    def attendance_percent(self):
        if not self.attendance:
            return 0
        return (self.attendance.count("P") / len(self.attendance)) * 100

    def to_line(self):
        return f"{self.student_id}|{self.subject_code}|grades={self.grades}|attendance={''.join(self.attendance)}"

    @staticmethod
    def from_line(line: str):
        parts = [p.strip() for p in line.strip().split("|")]
        student_id = parts[0]
        subject_code = parts[1]
        grades = []
        attendance = []
        for field in parts[2:]:
            if field.startswith("grades="):
                try:
                    grades = eval(field.split("=", 1)[1])
                except:
                    grades = []
            elif field.startswith("attendance="):
                attendance = list(field.split("=", 1)[1])
        return Record(student_id, subject_code, grades, attendance)
