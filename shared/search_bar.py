def build_search_bar_context(
    name: str, values: list[dict], placeholder: str = "Search...", selected_value: dict | None = None
) -> dict:
    return {
        "name": name,
        "values": values,
        "placeholder": placeholder,
        "selected_value": selected_value,
    }
