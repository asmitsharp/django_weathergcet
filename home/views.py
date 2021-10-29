from django.shortcuts import render
from pip._vendor import requests

def home(request):

    city = request.GET.get('city', "Delhi")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=86c2b10cd00e125870cb9103d5a975ab'
    urlf= f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=86c2b10cd00e125870cb9103d5a975ab'
    data = requests.get(url).json()
    forecast = requests.get(urlf).json()
    
    
    payload = { 
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin_temperature' : data['main']['temp'],
        'celcius_temperature' : int(data['main']['temp']-273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'main' : data['weather'][0]['main'],
        'description' : data['weather'][0]['description'],
        'visibility' : int(data['visibility']/1000),
        'feelslike' : int(data['main']['feels_like']-273)
    }

    foreload = {
        'date' : forecast['list'][0]['dt_txt'],
        'date1' : forecast['list'][1]['dt_txt'],
        'date2' : forecast['list'][2]['dt_txt'],
        'date3' : forecast['list'][3]['dt_txt'],
        'minTemp': int(forecast['list'][0]['main']['temp_min']-273),
        'minTemp1': int(forecast['list'][1]['main']['temp_min']-273),
        'minTemp2': int(forecast['list'][2]['main']['temp_min']-273),
        'minTemp3': int(forecast['list'][3]['main']['temp_min']-273),
        'maxTemp': int(forecast['list'][0]['main']['temp_max']-273),
        'maxTemp1': int(forecast['list'][1]['main']['temp_max']-273),
        'maxTemp2': int(forecast['list'][2]['main']['temp_max']-273),
        'maxTemp3': int(forecast['list'][3]['main']['temp_max']-273),
        'vis': int(forecast['list'][0]['visibility'])/1000,
        'vis1': int(forecast['list'][1]['visibility'])/1000,
        'vis2': int(forecast['list'][2]['visibility'])/1000,
        'vis3': int(forecast['list'][3]['visibility'])/1000,
    }

    context = {'data' : payload,
               'forecast' : foreload 
     }

    return render(request,"home.html", context)