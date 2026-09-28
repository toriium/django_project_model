from pydantic import BaseModel


def build_static_table_context(table_name: str, values: list[BaseModel], description: str = "") -> dict:
    if not values:
        columns = []
        data = []
    else:
        # Assume all items are the same model
        columns = list(values[0].model_fields.keys())
        data = [list(v.model_dump().values()) for v in values]
    return {
        "table_type": "static",
        "table_name": table_name,
        "columns": columns,
        "data": data,
        "description": description,
    }


def build_dynamic_table_context(table_name: str, url_name: str, description: str = "") -> dict:
    return {
        "table_type": "dynamic",
        "table_name": table_name,
        "url_name": url_name,
        "description": description,
    }
