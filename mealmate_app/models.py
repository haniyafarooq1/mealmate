from django.db import models
from django.contrib.auth.models import User

# ✅ Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    average_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name

# ✅ Recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()
    estimated_time = models.IntegerField(help_text="Time in minutes")
    
    def __str__(self):
        return self.title

# ✅ Favorite model — links users to their favorite restaurants or recipes
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mealmate_favorites')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Favorite"

