import pytest

from coffee_report.reporting import get_report_builder
from coffee_report.reports.median_coffee import build_report


def test_get_report_builder_returns_median_coffee_report():
    assert get_report_builder("median-coffee") == build_report


def test_get_report_builder_raises_for_unknown_report():
    with pytest.raises(ValueError, match="Неизвестный отчёт"):
        get_report_builder("unknown-report")
