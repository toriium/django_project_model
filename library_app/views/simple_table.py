from django.shortcuts import render
from pydantic import BaseModel

from components.tables import build_static_simple_table_context


class ColorTable(BaseModel):
    name: str
    value: int


def simple_table(request):
    color_list: list[ColorTable] = [
        ColorTable(name="Red", value=1),
        ColorTable(name="Green", value=2),
        ColorTable(name="Blue", value=3),
    ]

    context = {
        "color_table": build_static_simple_table_context(table_name="color", values=color_list),
    }
    return render(request, "library_app/simple_table.html", context)
