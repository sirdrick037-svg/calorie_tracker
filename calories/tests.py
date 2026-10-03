from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import FoodItem


class FoodItemViewsTests(TestCase):
    def test_home_shows_today_items_and_calorie_total(self):
        FoodItem.objects.create(name="Oats", calories=150)
        FoodItem.objects.create(name="Apple", calories=80)

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oats")
        self.assertContains(response, "Apple")
        self.assertEqual(response.context["total_calories"], 230)

    def test_add_food(self):
        response = self.client.post(
            reverse("add_food"),
            {"name": "Banana", "calories": 105},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(
            FoodItem.objects.filter(name="Banana", calories=105).exists()
        )

    def test_edit_food(self):
        food_item = FoodItem.objects.create(name="Oats", calories=150)

        response = self.client.post(
            reverse("edit_food", args=[food_item.pk]),
            {"name": "Overnight oats", "calories": 200},
        )

        self.assertRedirects(response, reverse("home"))
        food_item.refresh_from_db()
        self.assertEqual(food_item.name, "Overnight oats")
        self.assertEqual(food_item.calories, 200)

    def test_delete_food_requires_confirmation(self):
        food_item = FoodItem.objects.create(name="Oats", calories=150)

        response = self.client.get(
            reverse("delete_food", args=[food_item.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oats")
        self.assertTrue(FoodItem.objects.filter(pk=food_item.pk).exists())

        response = self.client.post(
            reverse("delete_food", args=[food_item.pk])
        )

        self.assertRedirects(response, reverse("home"))
        self.assertFalse(FoodItem.objects.filter(pk=food_item.pk).exists())

    def test_reset_today_removes_only_today_items(self):
        today_item = FoodItem.objects.create(name="Today", calories=100)
        older_item = FoodItem.objects.create(name="Yesterday", calories=90)
        FoodItem.objects.filter(pk=older_item.pk).update(
            date_added=timezone.localdate() - timedelta(days=1)
        )

        response = self.client.post(reverse("reset_today"))

        self.assertRedirects(response, reverse("home"))
        self.assertFalse(FoodItem.objects.filter(pk=today_item.pk).exists())
        self.assertTrue(FoodItem.objects.filter(pk=older_item.pk).exists())
