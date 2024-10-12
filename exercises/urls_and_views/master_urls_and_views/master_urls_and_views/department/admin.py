from django.contrib import admin

from master_urls_and_views.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
