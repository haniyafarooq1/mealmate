from django.db import models
from django.contrib.auth.models import User
from .recipe import Recipe

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ❤️ {self.recipe.title}"
