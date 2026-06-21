from datetime import date, datetime

from django.http import Http404
from django.shortcuts import render
from pydantic import BaseModel


# Create your views here.
def home(request):
    return render(request, "library_app/home.html")


def generate_generic_table(request, values: list[BaseModel]):
    if not values:
        columns = []
        data = []
    else:
        # Assume all items are the same model
        columns = list(values[0].model_fields.keys())
        data = [list(v.model_dump().values()) for v in values]
    context = {
        "columns": columns,
        "data": data,
    }
    return render(request, "library_app/generate_generic_table.html", context)


def people_table(request):
    class PeopleTable(BaseModel):
        name: str
        age: int
        birthday: date
        created_at: datetime
        active: bool

    people = [
        PeopleTable(
            name="Alice",
            age=30,
            birthday=date(1993, 5, 15),
            created_at=datetime(2023, 1, 1, 10, 0, 0),
            active=True,
        ),
        PeopleTable(
            name="Bob",
            age=25,
            birthday=date(1998, 8, 22),
            created_at=datetime(2023, 1, 2, 11, 0, 0),
            active=False,
        ),
        PeopleTable(
            name="Charlie",
            age=35,
            birthday=date(1988, 3, 10),
            created_at=datetime(2023, 1, 3, 12, 0, 0),
            active=True,
        ),
    ]
    return generate_generic_table(request, people)


def trigger_404(request):
    raise Http404("This page does not exist.")


def trigger_500(request):
    raise Exception("Intentional server error for testing.")
