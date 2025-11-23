
from django.shortcuts import render
from .models import Restaurant, Recipe
import random

def home(request):
    return render(request, 'mealmate_app/home.html')

def decision_flow(request):
    """Main decision flow - Eat Out vs Cook at Home"""
    if request.method == 'POST':
        choice = request.POST.get('choice')
        
        if choice == 'eat_out':
            return render(request, 'mealmate_app/cuisine_selection.html')
        elif choice == 'cook_home':
            return render(request, 'mealmate_app/meal_type_selection.html')
        elif choice == 'surprise_me':
            return surprise_me(request)
    
    return render(request, 'mealmate_app/decision_flow.html')

def cuisine_selection(request):
    unique_cuisines = Restaurant.objects.values_list('cuisine', flat=True).distinct()

    print("DEBUG — cuisines in DB:", list(unique_cuisines))

    if request.method == 'POST':
        cuisine = request.POST.get('cuisine')
        print("DEBUG — user selected:", cuisine)

        restaurants = Restaurant.objects.filter(cuisine__iexact=cuisine)
        print("DEBUG — restaurants found:", restaurants.count())

        return render(request, 'mealmate_app/restaurant_results.html', {
            'restaurants': restaurants,
            'cuisine': cuisine
        })

    # ✅ THIS WAS MISSING!!!
    return render(request, 'mealmate_app/cuisine_selection.html', {
        "unique_cuisines": unique_cuisines
    })


def meal_type_selection(request):
    """Handle meal type selection for recipes"""
    if request.method == 'POST':
        meal_type = request.POST.get('meal_type')
        recipes = Recipe.objects.filter(meal_type__iexact=meal_type)
        return render(request, 'mealmate_app/recipe_results.html', {
            'recipes': recipes,
            'meal_type': meal_type
        })
    
    return render(request, 'mealmate_app/meal_type_selection.html')

def surprise_me(request):
    """Surprise me feature - random recommendation"""
    all_restaurants = list(Restaurant.objects.all())
    all_recipes = list(Recipe.objects.all())
    
    # Randomly choose between restaurant or recipe
    if random.choice([True, False]) and all_restaurants:
        choice = random.choice(all_restaurants)
        choice_type = 'restaurant'
    elif all_recipes:
        choice = random.choice(all_recipes)
        choice_type = 'recipe'
    else:
        choice = None
        choice_type = None
    
    return render(request, 'mealmate_app/surprise_results.html', {
        'choice': choice,
        'choice_type': choice_type
    })


def debug_restaurants(request):
    """Temporary view to see all restaurants in database"""
    all_restaurants = Restaurant.objects.all()
    return render(request, 'mealmate_app/debug_restaurants.html', {
        'restaurants': all_restaurants
    })