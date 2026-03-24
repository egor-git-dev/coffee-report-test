from coffee_report.models import StudentRecord
from coffee_report.reports.median_coffee import build_report


def test_build_report_returns_students_sorted_by_median_desc():
    records = [
        StudentRecord(
            student="Алексей Смирнов",
            date="2024-06-01",
            coffee_spent=450,
            sleep_hours=4.5,
            study_hours=12,
            mood="норм",
            exam="Математика",
        ),
        StudentRecord(
            student="Алексей Смирнов",
            date="2024-06-02",
            coffee_spent=500,
            sleep_hours=4.0,
            study_hours=14,
            mood="устал",
            exam="Математика",
        ),
        StudentRecord(
            student="Алексей Смирнов",
            date="2024-06-03",
            coffee_spent=550,
            sleep_hours=3.5,
            study_hours=16,
            mood="зомби",
            exam="Математика",
        ),
        StudentRecord(
            student="Дарья Петрова",
            date="2024-06-01",
            coffee_spent=200,
            sleep_hours=7.0,
            study_hours=6,
            mood="отл",
            exam="Математика",
        ),
        StudentRecord(
            student="Дарья Петрова",
            date="2024-06-02",
            coffee_spent=250,
            sleep_hours=6.5,
            study_hours=8,
            mood="норм",
            exam="Математика",
        ),
        StudentRecord(
            student="Дарья Петрова",
            date="2024-06-03",
            coffee_spent=300,
            sleep_hours=6.0,
            study_hours=9,
            mood="норм",
            exam="Математика",
        ),
        StudentRecord(
            student="Иван Кузнецов",
            date="2024-06-01",
            coffee_spent=600,
            sleep_hours=3.0,
            study_hours=15,
            mood="зомби",
            exam="Математика",
        ),
        StudentRecord(
            student="Иван Кузнецов",
            date="2024-06-02",
            coffee_spent=650,
            sleep_hours=2.5,
            study_hours=17,
            mood="зомби",
            exam="Математика",
        ),
        StudentRecord(
            student="Иван Кузнецов",
            date="2024-06-03",
            coffee_spent=700,
            sleep_hours=2.0,
            study_hours=18,
            mood="не выжил",
            exam="Математика",
        ),
    ]
    
    report = build_report(records)
    
    assert report == [
        ("Иван Кузнецов", 650),
        ("Алексей Смирнов", 500),
        ("Дарья Петрова", 250),
    ]


def test_build_report_calculates_median_for_even_number_of_values():
    records = [
        StudentRecord(
            student="Мария Соколова",
            date="2024-06-01",
            coffee_spent=100,
            sleep_hours=8.0,
            study_hours=3,
            mood="отл",
            exam="Математика",
        ),
        StudentRecord(
            student="Мария Соколова",
            date="2024-06-02",
            coffee_spent=200,
            sleep_hours=8.0,
            study_hours=4,
            mood="отл",
            exam="Математика",
        ),
        StudentRecord(
            student="Мария Соколова",
            date="2024-06-03",
            coffee_spent=300,
            sleep_hours=7.5,
            study_hours=5,
            mood="норм",
            exam="Математика",
        ),
        StudentRecord(
            student="Мария Соколова",
            date="2024-06-04",
            coffee_spent=400,
            sleep_hours=7.0,
            study_hours=6,
            mood="устал",
            exam="Математика",
        ),
    ]

    report = build_report(records)

    assert report == [("Мария Соколова", 250.0)]
