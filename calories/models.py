from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=200)

    calories = models.PositiveIntegerField()

    date_added = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ["-id"]


    def __str__(self):
        return self.name