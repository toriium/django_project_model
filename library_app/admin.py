from django.contrib import admin
from advanced_filters.admin import AdvancedFilterAdmin, AdminAdvancedFiltersMixin


# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    advanced_filter_fields = ("title",'author')
    list_filter = [field.name for field in Book._meta.fields]
    search_fields = ('title', 'author')