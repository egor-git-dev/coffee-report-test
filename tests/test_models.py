from coffee_report.models import StudentRecord


def test_student_record_from_dict_converts_values():
    row = {
        "student": "Алексей Смирнов",
        "date": "2024-06-01",
        "coffee_spent": "450",
        "sleep_hours": "4.5",
        "study_hours": "12",
        "mood": "норм",
        "exam": "Математика",
    }
    
    record = StudentRecord.from_dict(row)
    
    assert record.student == "Алексей Смирнов"
    assert record.date == "2024-06-01"
    assert record.coffee_spent == 450
    assert record.sleep_hours == 4.5
    assert record.study_hours == 12
    assert record.mood == "норм"
    assert record.exam == "Математика"
    
    assert isinstance(record.coffee_spent, int)
    assert isinstance(record.sleep_hours, float)
    assert isinstance(record.study_hours, int)
