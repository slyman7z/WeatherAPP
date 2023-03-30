from django.shortcuts import render

# Create your views here.
import urllib.request    #Takes care of post request to API
import json             #Takes care of conversion from json to python library 


def index(request):
    
    if request.method == "POST":  #Takes care of request from form
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=598e31b472a984894f4f017dd554a005').read()  #Takes care of API source
        
        list_of_data = json.loads(source)  #Takes care of conversion from json to python library 
        context = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' , ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' c',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
    } # 
    
    else:
        context = {}
    
        
    return render(request, 'partials/index.html', context)