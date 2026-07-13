from django import template
from django.urls import reverse
from pydantic import BaseModel

register = template.Library()


class NavItem(BaseModel):
    label: str
    icon: str
    url_path: str | None = None
    url_name: str | None = None
    new_tab: bool = False

    def href(self):
        if self.url_name:
            return reverse(self.url_name)
        return self.url_path


class NavGroup(NavItem):
    nav_items_list: list[NavItem]


class Icons:
    HOME = "bi-house"
    TABLES = "bi-database"
    BOOKS = "bi-book"
    PEOPLE = "bi-people"
    DJANGO_ADMIN = "bi-gear"
    PUBLIC_PAGE = "bi-globe"
    TEST_404 = "bi-exclamation-triangle"
    TEST_500 = "bi-exclamation-octagon"


@register.simple_tag
def get_nav_items() -> list[NavItem| NavGroup]:
    home_nav = NavItem(
        label="Home",
        icon=Icons.HOME,
        url_name="home",
    )
    tebles_children = [
        NavItem(
            label="Books",
            icon=Icons.BOOKS,
            url_name="books_table",
        ),
        NavItem(
            label="People",
            icon=Icons.PEOPLE,
            url_name="people_table",
        ),
    ]
    tables_nav = NavGroup(
        label="Tables",
        icon=Icons.TABLES,
        nav_items_list=tebles_children,
    )
    django_admin_nav = NavItem(
        label="Django Admin",
        icon=Icons.DJANGO_ADMIN,
        url_path="/admin/",
        new_tab=True,
    )
    public_page_nav = NavItem(
        label="Public Page",
        icon=Icons.PUBLIC_PAGE,
        url_name="public",
    )
    test_404_nav = NavItem(
        label="Test 404",
        icon=Icons.TEST_404,
        url_name="trigger_404",
    )
    test_500_nav = NavItem(
        label="Test 500",
        icon=Icons.TEST_500,
        url_name="trigger_500",
    )
    return [
        home_nav,
        tables_nav,
        django_admin_nav,
        public_page_nav,
        test_404_nav,
        test_500_nav,
    ]


@register.simple_tag(takes_context=True)
def nav_active_class(context, href):
    if href and context["request"].path == href:
        return "active bg-primary text-white"
    return "text-light"