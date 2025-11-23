from django.contrib import admin
from .models import Restaurant, Recipe, FavoriteRecipe, FavoriteRestaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'location', 'average_price']
    list_filter = ['cuisine']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'meal_type', 'estimated_time']
    list_filter = ['meal_type']

@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe']

@admin.register(FavoriteRestaurant)
class FavoriteRestaurantAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant']

