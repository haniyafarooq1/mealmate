from django.db import models
from django.contrib.auth.models import User
from .restaurant import Restaurant

class FavoriteRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_restaurants')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ❤️ {self.restaurant.name}"
