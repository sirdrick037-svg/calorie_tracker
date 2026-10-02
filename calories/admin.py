from django.contrib import admin
from .models import FoodItem

# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "calories",
        "date_added",
    )

    list_filter = (
        "date_added",
    )

    search_fields = (
        "name",
    )