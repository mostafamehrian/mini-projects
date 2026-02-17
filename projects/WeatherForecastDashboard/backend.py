import requests
from datetime import date, timedelta

API_KEY = 'b7005a99d79680498e809649704f3094'

def getdata(place,days,kind):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    
    response = requests.get(url)
    contenet = response.json()
    
    today = date.today() + timedelta(days=1)

    dates = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days)]
    templist = []
    timelist = []
    weatherlist = []
    weatherdesclist = []
    for day in dates:
        predictiondict = contenet['list']
        for predict in predictiondict:
            if predict['dt_txt'].split()[0] == day:
                if kind == 'Temperture':
                    tempfarenhite = predict['main']['temp']
            
                    tempcelsiuse = (tempfarenhite - 273.15)
                    templist.append(tempcelsiuse)
                    timelist.append(predict['dt_txt'])
                    
                
                elif kind == 'Sky':
                    weathermain = predict['weather'][0]['main']
                    weather_description = predict['weather'][0]['description']
                    weatherlist.append(weathermain)
                    weatherdesclist.append(weather_description)
                    
                    
                    
        
    if kind == 'Temperture':
        return timelist , templist     
    elif kind == 'Sky':
        return weatherlist , weatherdesclist

