from django.shortcuts import render
from pydantic import BaseModel


def generate_generic_table(request, table_name: str, values: list[BaseModel]):
    if not values:
        columns = []
        data = []
    else:
        # Assume all items are the same model
        columns = list(values[0].model_fields.keys())
        data = [list(v.model_dump().values()) for v in values]
    context = {
        "table_name": table_name,
        "columns": columns,
        "data": data,
    }
    return render(request, "library_app/generic_table.html", context)
