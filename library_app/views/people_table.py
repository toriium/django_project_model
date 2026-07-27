from datetime import date, datetime

from django.shortcuts import render
from pydantic import BaseModel

from library_app.views.shared_views import build_static_table_context


class PeopleTable(BaseModel):
    name: str
    age: int
    birthday: date
    created_at: datetime
    active: bool


def people_table(request):
    people_list = [
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
            name="Charlie", age=35, birthday=date(1988, 3, 10), created_at=datetime(2023, 1, 3, 12, 0, 0), active=True
        ),
        *[
            PeopleTable(
                name=f"Person {i}",
                age=i,
                birthday=date(1993, 5, 15),
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                active=True,
            )
            for i in range(1, 200)
        ],
    ]

    table_context = build_static_table_context(
        table_name="People", values=people_list, description="Table containing random people data for testing purposes."
    )
    context = {"table": table_context}
    return render(request, "library_app/people_table.html", context)
