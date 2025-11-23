

from django.db import models
from django.contrib.auth.models import User


# -------------------------------
# Restaurant and related models
# -------------------------------
class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    price_range = models.CharField(max_length=50)
    discount = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------------------
# Recipe and ingredient models
# -------------------------------
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    meal_type = models.CharField(max_length=50, choices=[
        ('Quick', 'Quick'),
        ('Fancy', 'Fancy'),
    ])
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.TextField()
    cook_time = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# -------------------------------
# User-related models
# -------------------------------
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s favorite"

