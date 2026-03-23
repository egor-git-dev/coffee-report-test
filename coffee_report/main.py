import sys

from tabulate import tabulate

from coffee_report.cli import parse_args
from coffee_report.loader import load_records
from coffee_report.reporting import get_report_builder


def main() -> None:
    try:
        args = parse_args()
        records = load_records(args.files)
        report_builder = get_report_builder(args.report)
        report_rows = report_builder(records)
        table = tabulate(
            report_rows,
            headers=["student", "median_coffee"],
            tablefmt="github",
        )
        print(table)

    except (FileNotFoundError, ValueError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
