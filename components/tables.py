from django.db import models
from pydantic import BaseModel

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
        # The search bar input shares the field name, so the GET may repeat a value or send an empty one
        selected = list(dict.fromkeys(value for value in request.GET.getlist(field.name) if value))

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

    columns = [field.name for field in fields]
    data = []
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
    }
