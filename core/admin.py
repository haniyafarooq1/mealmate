

from django.contrib import admin
from .models import Cuisine, Restaurant, Ingredient, Recipe, Favorite


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cuisine', 'location', 'price_range', 'discount')
    list_filter = ('cuisine',)
    search_fields = ('name', 'location')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'meal_type', 'cook_time')
    list_filter = ('meal_type',)
    search_fields = ('title',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'restaurant')

