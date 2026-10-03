from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone

from .models import FoodItem
from calorie_tracker.forms import FoodItemForm

# Create your views here.
def home(request):

    today = timezone.localdate()

    food_items = FoodItem.objects.filter(
        date_added=today
    )

    total_calories = (
        food_items.aggregate(
            total=Sum("calories")
        )["total"]
        or 0
    )

    context = {
        "food_items": food_items,
        "total_calories": total_calories,
        "today": today,
    }

    return render(
        request,
        "calorie_tracker/home.html",
        context
    )


def add_food(request):

    if request.method == "POST":

        form = FoodItemForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Food item added successfully."
            )

            return redirect("home")

    else:

        form = FoodItemForm()

    return render(
        request,
        "calorie_tracker/food_form.html",
        {
            "form": form,
            "title": "Add Food",
            "button_text": "Add Food",
        }
    )

def edit_food(request, food_id):

    food_item = get_object_or_404(
        FoodItem,
        id=food_id
    )

    if request.method == "POST":

        form = FoodItemForm(
            request.POST,
            instance=food_item
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Food item updated successfully."
            )

            return redirect("home")

    else:

        form = FoodItemForm(
            instance=food_item
        )

    return render(
        request,
        "calorie_tracker/food_form.html",
        {
            "form": form,
            "title": "Edit Food",
            "button_text": "Save Changes",
        }
    )


def delete_food(request, food_id):

    food_item = get_object_or_404(
        FoodItem,
        id=food_id
    )

    if request.method == "POST":

        food_item.delete()

        messages.success(
            request,
            "Food item removed successfully."
        )

        return redirect("home")

    return render(
        request,
        "calorie_tracker/food_confirm_delete.html",
        {
            "food_item": food_item
        }
    )


def reset_today(request):

    if request.method == "POST":

        today = timezone.localdate()

        FoodItem.objects.filter(
            date_added=today
        ).delete()

        messages.success(
            request,
            "Today's calorie count has been reset."
        )

    return redirect("home")