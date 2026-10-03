from datetime import date

from django.db import models
from pydantic import BaseModel

from components.date_range import build_date_range_context
from components.search_bar import build_search_bar_context


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

def build_static_simple_table_context(table_name: str, values: list[BaseModel], description: str = "") -> dict:
    columns = list(values[0].model_fields.keys()) if values else []
    data = [list(v.model_dump().values()) for v in values]
    return {
        "table_type": "simple",
        "table_name": table_name,
        "columns": columns,
        "data": data,
        "description": description,
    }


def build_static_autofilter_model_table_context(
    request, model: type[models.Model], table_name: str, description: str = ""
) -> dict:
    fields = [field for field in model._meta.fields if field.name not in ("id", "created_at", "updated_at")]
    text_fields = [
        field for field in fields if isinstance(field, (models.CharField, models.TextField, models.ForeignKey))
    ]

    queryset = model.objects.select_related(*[field.name for field in fields if field.is_relation])
    filters = []
    for field in text_fields:
        selected = request.GET.getlist(field.name)

        if field.is_relation:
            # Related objects are shown and filtered by their str(), mapped back to primary keys for the query
            related = field.related_model.objects.filter(pk__in=model.objects.values(field.attname))
            pk_by_label = {str(obj): obj.pk for obj in related}
            labels = sorted(pk_by_label)
            if selected:
                queryset = queryset.filter(**{f"{field.attname}__in": [pk_by_label.get(label) for label in selected]})
        else:
            labels = list(
                model.objects.exclude(**{field.name: ""})
                .order_by(field.name)
                .values_list(field.name, flat=True)
                .distinct()
            )
            if selected:
                queryset = queryset.filter(**{f"{field.name}__in": selected})

        search_bar = build_search_bar_context(name=field.name, values=[{"label": label} for label in labels])
        filters.append({"search_bar": search_bar, "selected": selected})

    date_filters = []
    for field in fields:
        if not isinstance(field, models.DateField):
            continue
        start_date = request.GET.get(f"{field.name}_start_date")
        end_date = request.GET.get(f"{field.name}_end_date")
        start_date = date.fromisoformat(start_date) if start_date else None
        end_date = date.fromisoformat(end_date) if end_date else None
        # DateTimeField is a DateField subclass; compare only its day so the range includes the end date
        lookup = f"{field.name}__date" if isinstance(field, models.DateTimeField) else field.name
        if start_date:
            queryset = queryset.filter(**{f"{lookup}__gte": start_date})
        if end_date:
            queryset = queryset.filter(**{f"{lookup}__lte": end_date})
        date_filters.append(build_date_range_context(name=field.name, start_date=start_date, end_date=end_date))

    columns = [field.name for field in fields]
    data = []
    # The table starts empty and only loads once the Filter button is clicked
    if "filtered" not in request.GET:
        queryset = queryset.none()
    for obj in queryset:
        row = []
        for field in fields:
            value = getattr(obj, field.name)
            row.append(str(value) if field.is_relation and value is not None else value)
        data.append(row)
    return {
        "table": {
            "table_type": "static",
            "table_name": table_name,
            "columns": columns,
            "data": data,
            "description": description,
        },
        "filters": filters,
        "date_filters": date_filters,
    }
