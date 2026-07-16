from django.shortcuts import render
from pydantic import BaseModel

from library_app.views.shared_views import build_table_context


class LiquidTable(BaseModel):
    name: str
    mls: int

class ColorTable(BaseModel):
    name: str
    value: int


def multi_table(request):
    color_list: list[ColorTable] = [
        ColorTable(name="Red", value=1),
        ColorTable(name="Green", value=2),
    ]

    liquid_list: list[LiquidTable] = [
        LiquidTable(name="Water", mls=500),
        LiquidTable(name="Juice", mls=300),
    ]

    color_context = build_table_context(table_name="color", values=color_list)
    liquid_context = build_table_context(table_name="liquid", values=liquid_list)
    context = {
        "color_table": color_context,
        "liquid_table": liquid_context,
    }
    return render(request, "library_app/multi_table.html", context)
