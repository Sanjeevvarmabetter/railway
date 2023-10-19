from django.shortcuts import render
from .models import Station
from django.shortcuts import redirect
from .models import Train
import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def display_stations(request):
    stations = Station.objects.all()
    return render(request,'display_stations.html',{'stations':stations})

def available_trains(request):
    station_id = request.POST.get('station_id')
    available_trains = Train.objects.filter(station_id = station_id)
    return render(request, 'available_trains.html', {'available_trains': available_trains})


def  book_train(request, train_id):
    selected_train = Train.objects.get(id=train_id)
    return render(request,'booking_form.html', {'selected_train': selected_train})

def get_train_live_status(request, train_number):
    api_key = 'enter api key'

    url = 'Enter url'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    
    else:
        return JsonResponse({'error': 'Failed to fetch live status'}, status=500)
    
