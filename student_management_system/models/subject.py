class Subject:
    def __init__(self, code: str, name: str, credit_hours: int):
        self.code = code.strip()
        self.name = name.strip()
        self.credit_hours = int(credit_hours)

    @staticmethod
    def from_line(line: str):
        parts = [p.strip() for p in line.strip().split("|")]
        if len(parts) < 3:
            raise ValueError("Bad subject line: " + line)
        return Subject(parts[0], parts[1], parts[2])

    def to_line(self) -> str:
        return f"{self.code} | {self.name} | {self.credit_hours}"

    def __repr__(self):
        return f"Subject({self.code}, {self.name}, {self.credit_hours})"
