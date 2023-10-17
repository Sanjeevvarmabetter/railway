from django.shortcuts import render
from .models import Station
from django.shortcuts import redirect
from .models import Train
# Create your views here.


def display_stations(request):
    stations = Station.objects.all()
    return render(request,'display_stations.html',{'stations':stations})

def available_trains(request):
    station_id = request.POST.get('station_id')

    available_trains = Train.objects.filter(station_id = station_id)
    return render(request, 'available_trains.html', {'available_trains': available_trains})