
from django.shortcuts import render  
import json 
import urllib.request 


def index(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 

	
		api = urllib.request.urlopen( 
			'http://api.openweathermap.org/data/2.5/weather?q='
					+ city + '&appid=a9f3f918ef4b146e0c7c1bf1b03a2014').read() 

		list_of_data = json.loads(api) 

		data = { 
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": 'Long. '+str(list_of_data['coord']['lon']) + '  '
						+ 'Lati. '+str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + ' K', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		}
        
        
    
	else: 
		data ={} 
	return render(request, "weather/index.html", data) 
