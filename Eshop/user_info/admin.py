from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "password",
        "city",
        "country",
        "Address",
        "profile_image",
        "phone_number",
        "birth_date",
    ]
    search_fields = ("first_name__startswith",)
