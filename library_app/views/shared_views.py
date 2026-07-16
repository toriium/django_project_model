from django.shortcuts import render
from pydantic import BaseModel


def build_table_context(table_name: str, values: list[BaseModel], description: str = "") -> dict:
    if not values:
        columns = []
        data = []
    else:
        # Assume all items are the same model
        columns = list(values[0].model_fields.keys())
        data = [list(v.model_dump().values()) for v in values]
    return {
        "table_name": table_name,
        "columns": columns,
        "data": data,
        "description": description,
    }


def generate_generic_table(request, table_name: str, values: list[BaseModel]):
    context = {"table": build_table_context(table_name, values)}
    return render(request, "library_app/table_page.html", context)
