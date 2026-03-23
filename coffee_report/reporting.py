from coffee_report.reports.median_coffee import build_report


REPORT_BUILDERS = {
    "median-coffee": build_report,
}


def get_report_builder(report_name: str):
    if report_name not in REPORT_BUILDERS:
        raise ValueError(f"Неизвестный отчёт: {report_name}")
    
    return REPORT_BUILDERS[report_name]
