from django.shortcuts import render
from pydantic import BaseModel

from components.tables import build_dynamic_table_context, build_static_table_context


def generate_static_table_html(request, table_name: str, values: list[BaseModel], description: str = ""):
    context = {"table": build_static_table_context(table_name=table_name, values=values, description=description)}
    return render(request, "library_app/table_page.html", context)


def generate_dynamic_table_html(request, table_name: str, url_name: str, description: str = ""):
    context = {"table": build_dynamic_table_context(table_name=table_name, url_name=url_name, description=description)}
    return render(request, "library_app/table_page.html", context)
