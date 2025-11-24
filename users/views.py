from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .services.suggestion import recipes_by_meal_type, recipes_by_ingredients
import random
from mealmate_app.models import FavoriteRestaurant, FavoriteRecipe, Restaurant, Recipe


# SIGNUP - using the form with email and password confirmation
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()        # creates user and hashes password
            login(request, user)      # log the user in immediately
            messages.success(request, f"Account created for {user.username}!")
            return redirect('home')   # redirect to users/home
        else:
            # form invalid: render form with errors
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


# LOGIN - simple version using AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')   
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# LOGOUT (simple)
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('landing')  # or '/' depending on your landing name






# existing imports should remain; add these views if they are not present

@login_required
def home_view(request):
    return render(request, 'users/home.html')


@login_required
def cook_view(request):
    """
    Suggest recipes based on meal type or ingredients entered by user.
    """
    from mealmate_app.models import Recipe  # ADD THIS IMPORT
    
    recipes = []
    meal_type = ''
    ingredients = ''

    if request.method == "POST":
        meal_type = request.POST.get('meal_type', '').strip()
        ingredients = request.POST.get('ingredients', '').strip()

        if meal_type:
            # Filter recipes from database by meal_type
            recipes = Recipe.objects.filter(meal_type__icontains=meal_type)
        elif ingredients:
            # Filter recipes that contain the ingredients
            recipes = Recipe.objects.filter(ingredients__icontains=ingredients)
        else:
            # Show all recipes if no filter
            recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
        'meal_type': meal_type,
        'ingredients': ingredients,
    }
    return render(request, 'users/cook.html', context)



@login_required
def eat_out_view(request):
    """
    Suggest nearby restaurants or types of cuisines to eat out.
    """
    restaurants = []
    cuisine = ''

    if request.method == "POST":
        cuisine = request.POST.get('cuisine', '').strip().lower()

        all_restaurants = [
            {"name": "Pizza Palace", "cuisine": "italian", "location": "Downtown"},
            {"name": "Sushi House", "cuisine": "japanese", "location": "City Center"},
            {"name": "Spice Hub", "cuisine": "indian", "location": "Main Street"},
            {"name": "Burger Shack", "cuisine": "american", "location": "Mall Road"},
            {"name": "Taco Fiesta", "cuisine": "mexican", "location": "Market Square"},
        ]

        if cuisine:
            restaurants = [r for r in all_restaurants if cuisine in r["cuisine"]]
        else:
            restaurants = all_restaurants

    context = {"restaurants": restaurants, "cuisine": cuisine}
    return render(request, 'users/eat_out.html', context)



@login_required

def surprise_view(request):
    """
    Randomly suggest a dish to cook or a restaurant to visit.
    """
    # Sample data for both options
    dishes = [
        "Spaghetti Bolognese", "Chicken Curry", "Grilled Cheese Sandwich",
        "Tacos", "Fried Rice", "Pasta Alfredo", "Homemade Pizza"
    ]

    restaurants = [
        "Pizza Palace", "Sushi House", "Spice Hub",
        "Burger Shack", "Taco Fiesta", "The Grill Point"
    ]

    suggestion_type = random.choice(["dish", "restaurant"])
    suggestion = random.choice(dishes) if suggestion_type == "dish" else random.choice(restaurants)

    context = {
        "suggestion_type": suggestion_type,
        "suggestion": suggestion
    }
    return render(request, 'users/surprise.html', context)


@login_required
def favorites_view(request):
    """Show user's favorite restaurants and recipes"""
    favorite_restaurants = FavoriteRestaurant.objects.filter(user=request.user)
    favorite_recipes = FavoriteRecipe.objects.filter(user=request.user)
    
    context = {
        'favorite_restaurants': favorite_restaurants,
        'favorite_recipes': favorite_recipes,
    }
    return render(request, 'users/favorites.html', context)

@login_required
def add_favorite_recipe(request):
    """Add a recipe to user's favorites"""
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        
        # Check if recipe_id is provided and is a valid number
        if not recipe_id or not recipe_id.isdigit():
            messages.error(request, "Invalid recipe selection!")
            return redirect(request.META.get('HTTP_REFERER', '/users/home/'))
        
        try:
            recipe = Recipe.objects.get(id=int(recipe_id))
            # Check if already favorited
            if not FavoriteRecipe.objects.filter(user=request.user, recipe=recipe).exists():
                FavoriteRecipe.objects.create(user=request.user, recipe=recipe)
                messages.success(request, f"Added {recipe.title} to favorites!")
            else:
                messages.info(request, f"{recipe.title} is already in your favorites!")
        except Recipe.DoesNotExist:
            messages.error(request, "Recipe not found!")
    
    # Go back to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/users/home/'))

@login_required
def add_favorite_restaurant(request):
    """Add a restaurant to user's favorites"""
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        
        # Check if restaurant_id is provided and is a valid number
        if not restaurant_id or not restaurant_id.isdigit():
            messages.error(request, "Invalid restaurant selection!")
            return redirect(request.META.get('HTTP_REFERER', '/users/home/'))
        
        try:
            restaurant = Restaurant.objects.get(id=int(restaurant_id))
            # Check if already favorited
            if not FavoriteRestaurant.objects.filter(user=request.user, restaurant=restaurant).exists():
                FavoriteRestaurant.objects.create(user=request.user, restaurant=restaurant)
                messages.success(request, f"Added {restaurant.name} to favorites!")
            else:
                messages.info(request, f"{restaurant.name} is already in your favorites!")
        except Restaurant.DoesNotExist:
            messages.error(request, "Restaurant not found!")
    
    # Go back to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/users/home/'))