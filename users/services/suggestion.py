# users/services/suggestion.py
from mealmate_app.models import Recipe
import re

def normalize_list(text):
    """Convert comma separated text to cleaned lowercase set"""
    if not text:
        return set()
    items = [i.strip().lower() for i in re.split(r',|\n', text) if i.strip()]
    return set(items)

def recipes_by_meal_type(meal_type):
    """
    Return QuerySet-like list of recipes matching the meal_type (case-insensitive).
    We return a Python list of model instances.
    """
    return Recipe.objects.filter(meal_type__iexact=meal_type)

def recipes_by_ingredients(available_text):
    """
    available_text: comma-separated ingredients string from user.
    We match recipes whose required ingredients are subset of available ingredients.
    This assumes Recipe.ingredients is a comma-separated text field.
    """
    have = normalize_list(available_text)
    matches = []
    for r in Recipe.objects.all():
        req = normalize_list(r.ingredients)
        # require that all required ingredients are in have OR at least some match:
        # choose subset to be strict: only show recipes we can fully make
        if req and req.issubset(have):
            matches.append(r)
    return matches
