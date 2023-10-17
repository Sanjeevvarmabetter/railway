from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_stations, name='home'),  # Update the empty path to point to display_stations
    path('display_stations/', views.display_stations, name='display_stations'),
     path('available_trains/', views.available_trains, name='available_trains'),
    # Add other URL patterns as needed
]
