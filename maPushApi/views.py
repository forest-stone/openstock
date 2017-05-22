from django.shortcuts import render
from django.http import HttpResponse
from stockScreener.models import stock

import json

# Create your views here.
def addStockCode(request):
    result = 0
    try:
        jsonString = request.GET['JSON']
        print (jsonString)
        dict = json.loads(jsonString)
        print(dict['stockCode'])

    except:
        print("Json error")
        # json error code : 2
        return HttpResponse("[{\"result\": 2}]")

    tempStock = stock(stockCode=dict['stockCode'], now=0 ,ma5=0, ma20=0, ma60=0)
    try:
        tempStock.save(force_insert=True)
        print("Save Stock")
        return HttpResponse("[{\"result\": 1}]")
    except:
        print("Stock already exist")
        return HttpResponse("[{\"result\": 3}]")

def showStockInfo(request):
    results = [stock.showStockInfo() for stock in stock.objects.all()]
    return HttpResponse(json.dumps(results, indent=4), content_type="application/json")
