from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json

    #For Price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,XLM,ADA,USDT&tsyms=INR")
    price = json.loads(price_request.content)

    #For news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):

    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()
        cry_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=INR")
        crypto = json.loads(cry_request.content)


        return render(request,'prices.html',{'quote':quote,'crypto':crypto})

    else:
        return render(request,'prices.html',{})
