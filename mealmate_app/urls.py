from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('mealmate_app.urls')),
    #path('', views.home, name='home'),
    path('decision/', views.decision_flow, name='decision_flow'),
    path('cuisine/', views.cuisine_selection, name='cuisine_selection'),
    path('meal-type/', views.meal_type_selection, name='meal_type_selection'),
    path('surprise/', views.surprise_me, name='surprise_me'),
    path('debug/', views.debug_restaurants, name='debug_restaurants'),
]