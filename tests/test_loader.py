import pytest

from coffee_report.loader import load_records
from coffee_report.models import StudentRecord


@pytest.fixture
def sample_csv_file(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text(
        """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
""",
        encoding="utf-8",
    )
    return file_path

def test_load_records_reads_single_file(sample_csv_file):
    records = load_records([str(sample_csv_file)])

    assert len(records) == 1

    record = records[0]

    assert isinstance(record, StudentRecord)
    assert record.student == "Алексей Смирнов"
    assert record.date == "2024-06-01"
    assert record.coffee_spent == 450
    assert record.sleep_hours == 4.5
    assert record.study_hours == 12
    assert record.mood == "норм"
    assert record.exam == "Математика"


def test_load_records_merges_multiple_files(tmp_path):
    file_one = tmp_path / "data1.csv"
    file_one.write_text(
        """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
""",
        encoding="utf-8",
    )

    file_two = tmp_path / "data2.csv"
    file_two.write_text(
        """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Дарья Петрова,2024-06-02,250,6.5,8,норм,Математика
""",
        encoding="utf-8",
    )

    records = load_records([str(file_one), str(file_two)])

    assert len(records) == 2

    students = [record.student for record in records]

    assert "Алексей Смирнов" in students
    assert "Дарья Петрова" in students


def test_load_records_raises_for_missing_file():
    with pytest.raises(FileNotFoundError):
        load_records(["missing.csv"])
