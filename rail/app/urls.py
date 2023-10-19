from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_stations, name='home'),  # Update the empty path to point to display_stations
    path('display_stations/', views.display_stations, name='display_stations'),
    path('available_trains/<int:from_station_id>/<int:to_station_id',views.available_trains, name='available_trains'),
    path('book_train/<int:train_id>/', views.book_train, name='book_train'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking'),

]
