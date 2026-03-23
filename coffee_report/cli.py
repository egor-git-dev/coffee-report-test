import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Сформировать отчёт по CSV-файлам с данными студентов."
    )
    
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к одному или нескольким файлам",
    )
    
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчёта",
    )
    
    return parser


def parse_args() -> argparse.Namespace:
    parser = build_parser()
    
    return parser.parse_args()
