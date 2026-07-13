from django import template
from django.urls import reverse

register = template.Library()


def _item(label, icon, url_name=None, path=None, new_tab=False, children=None):
    href = reverse(url_name) if url_name else path
    return {"label": label, "icon": icon, "href": href, "new_tab": new_tab, "children": children or []}


@register.simple_tag
def get_nav_items():
    return [
        _item("Home", "&#8962;", url_name="home"),
        _item(
            "Tables",
            "&#128202;",
            children=[
                _item("Books", "&#128279;", url_name="books_table"),
                _item("People", "&#128100;", url_name="people_table"),
            ],
        ),
        _item("Django Admin", "&#9881;", path="/admin/", new_tab=True),
        _item("Public Page", "&#127760;", url_name="public"),
        _item("Test 404", "&#9888;", url_name="trigger_404"),
        _item("Test 500", "&#128165;", url_name="trigger_500"),
    ]


@register.simple_tag(takes_context=True)
def nav_active_class(context, href):
    if href and context["request"].path == href:
        return "active bg-primary text-white"
    return "text-light"
