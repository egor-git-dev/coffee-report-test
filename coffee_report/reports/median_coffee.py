from statistics import median

from coffee_report.models import StudentRecord


def build_report(records: list[StudentRecord]) -> list[tuple[str, float]]:
    student_coffee_spendings: dict[str, list[int]] = {}
    
    for record in records:
        if record.student not in student_coffee_spendings:
            student_coffee_spendings[record.student] = []
            
        student_coffee_spendings[record.student].append(record.coffee_spent)
    
    report_rows: list[tuple[str, float]] = []
    
    for student, spending_values in student_coffee_spendings.items():
        median_spent = median(spending_values)
        report_rows.append((student, median_spent))
    
    report_rows.sort(key=lambda row: row[1], reverse=True)
    
    return report_rows
