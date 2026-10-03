from datetime import date


def build_date_range_context(name: str, start_date: date | None = None, end_date: date | None = None) -> dict:
    return {
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
    }
