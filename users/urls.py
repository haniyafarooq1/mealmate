from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('cook/', views.cook_view, name='cook'),
    path('eat-out/', views.eat_out_view, name='eat_out'),
    path('surprise/', views.surprise_view, name='surprise'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/add-restaurant/', views.add_favorite_restaurant, name='add_favorite_restaurant'),
    path('favorites/add-recipe/', views.add_favorite_recipe, name='add_favorite_recipe'),
]




