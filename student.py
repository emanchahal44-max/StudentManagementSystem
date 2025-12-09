class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section

    def to_line(self):
        return f"{self.student_id} | {self.name} | {self.section}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("|")
        if len(parts) < 3:
            raise ValueError("Bad student line: " + line)
        student_id = parts[0].strip()
        name = parts[1].strip()
        section = parts[2].strip()
        return Student(student_id, name, section)
