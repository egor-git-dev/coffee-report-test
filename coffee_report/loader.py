import csv
from pathlib import Path

from coffee_report.models import StudentRecord


def load_records(file_paths: list[str]) -> list[StudentRecord]:
    records: list[StudentRecord] = []
    
    for file_path in file_paths:
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        
        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                record = StudentRecord.from_dict(row)
                records.append(record)
    
    return records
