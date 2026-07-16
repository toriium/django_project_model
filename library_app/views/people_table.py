from datetime import date, datetime

from pydantic import BaseModel

from library_app.views.shared_views import generate_generic_table


def people_table(request):
    class PeopleTable(BaseModel):
        name: str
        age: int
        birthday: date
        created_at: datetime
        active: bool

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

    return generate_generic_table(request, table_name="People", values=people_list)
