from django.shortcuts import render
import requests


# Create your views here.
def AsosiySahifaView(request):
    url = "https://currency-exchange.p.rapidapi.com/exchange"
    querystring = {"from":"USD","to":"UZS","q":"1.0"}
    headers = {
        "X-RapidAPI-Key": "f4152adb40mshddc3034080b186bp18b494jsn1bd9726ff216",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    natija = response.json() # 12281.49 
    
    context = {
        'usd': natija
    }
    
    return render(request, 'index.html',context)