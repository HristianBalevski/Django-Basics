from django.contrib import admin

from my_tennis_club.members.models import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "joined_date")