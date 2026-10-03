from django import forms

from calories.models import FoodItem


class FoodItemForm(forms.ModelForm):

    class Meta:
        model = FoodItem

        fields = [
            "name",
            "calories",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-gray-300 "
                        "px-4 py-3 focus:border-indigo-500 "
                        "focus:outline-none focus:ring-2 "
                        "focus:ring-indigo-200"
                    ),
                    "placeholder": "e.g. Chicken",
                }
            ),

            "calories": forms.NumberInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-gray-300 "
                        "px-4 py-3 focus:border-indigo-500 "
                        "focus:outline-none focus:ring-2 "
                        "focus:ring-indigo-200"
                    ),
                    "placeholder": "e.g. 450",
                    "min": "0",
                }
            ),
        }