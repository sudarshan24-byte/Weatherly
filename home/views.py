from django.shortcuts import render
import requests
import datetime
# Create your views here.
# a86236dacffd8ba400f85495ee8233b1
# Website Link: 

def home(request):
    api = 'a86236dacffd8ba400f85495ee8233b1'

    today = datetime.date.today()
    formatted_date = today.strftime("%A, %d %B %Y")

    # Fetching latitude and longitude
    city = request.GET.get('city')
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api}"
    r = requests.get(url).json()
    payload = {'lat': r[0]['lat'], 'lon': r[0]['lon']}
    lat = payload['lat']
    lon = payload['lon']

    # Main URL
    mainUrl = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
    response = requests.get(mainUrl).json()

    kelvin = response['main']['temp']
    c = kelvin - 273.15
    f = (c)*9/5 + 32

    #Celcius
    splitCel = str(c).split('.')
    celsius = splitCel[0]
    
    #Fahrenheit
    splitFah = str(f).split('.')
    fahrenheit = splitFah[0]

    contents = {'city': response['name'], 
                'tempCel': celsius, 
                'tempFah': fahrenheit, 
                'country': response['sys']['country'],
                'humidity': response['main']['humidity'],
                'pressure': response['main']['pressure'],
                'icon': response['weather'][0]['icon'],
                'description': response['weather'][0]['description'],
                'date': formatted_date
            }
    try:
      print(contents)
    except Exception as e:
       print('Error: ', e)

    return render(request, 'home.html', contents)