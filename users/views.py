from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .services.suggestion import recipes_by_meal_type, recipes_by_ingredients
import random


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
    recipes = []
    meal_type = ''
    ingredients = ''

    if request.method == "POST":
        meal_type = request.POST.get('meal_type', '').strip()
        ingredients = request.POST.get('ingredients', '').strip()

        if meal_type:
            recipes = recipes_by_meal_type(meal_type)
        elif ingredients:
            recipes = recipes_by_ingredients(ingredients)

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





