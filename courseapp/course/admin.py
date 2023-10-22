from django.contrib import admin
from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    list_per_page = 3
    search_help_text = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)