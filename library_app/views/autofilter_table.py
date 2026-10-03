from django.shortcuts import render

from components.tables import build_static_autofilter_model_table_context
from ..models import Book


def autofilter_table(request):
    context = build_static_autofilter_model_table_context(request, model=Book, table_name="Books")
    return render(request, "library_app/autofilter_table.html", context)
