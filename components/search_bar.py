def build_search_bar_context(name: str, values: list[str], placeholder: str = "Search...") -> dict:
    return {
        "name": name,
        "values": values,
        "placeholder": placeholder,
    }
