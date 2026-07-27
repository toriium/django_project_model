from .shared_views import generate_dynamic_table_html


def authors_table(request):
    return generate_dynamic_table_html(request, table_name="Authors", url_name="/api/authors")
