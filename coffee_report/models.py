from dataclasses import dataclass


@dataclass
class StudentRecord:
    student: str
    date: str
    coffee_spent: int
    sleep_hours: float
    study_hours: int
    mood: str
    exam: str

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "StudentRecord":
        return cls(
            student=row["student"],
            date=row["date"],
            coffee_spent=int(row["coffee_spent"]),
            sleep_hours=float(row["sleep_hours"]),
            study_hours=int(row["study_hours"]),
            mood=row["mood"],
            exam=row["exam"],
        )
