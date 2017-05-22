from django.shortcuts import render
from django.http import HttpResponse
from .models import stock
import time
import json

# Create your tests here.

stopScreen = False

def startStockNow(request):
    print("startStockNow - start")
    global stopScreen
    stopScreen = False

    while(1) :
        print(stopScreen)
        if(stopScreen):
            break

        for stocktemp in stock.objects.all() :
            stocktemp.checkStockNow()
        time.sleep(10)

def stopStockNow(request):
    print("stopStockNow - start")
    global stopScreen

    stopScreen = True
    print(stopScreen)
    return HttpResponse("")

def startStockMA(request):
    print("startStockMA - start")
    for stocktemp in stock.objects.all() :
        stocktemp.checkStockMA()
    return HttpResponse("")

def addStockCode(request):
    print("addStockCode - start")
    try:
        jsonString = request.GET['JSON']
        print (jsonString)
        dict = json.loads(jsonString)
        print("addStockCode - code : " + dict['stockCode'])

    except:
        print("addStockCode - Json error")
        # json error code : 2
        return HttpResponse("[{\"result\": 2}]")

    tempStock = stock(stockCode=dict['stockCode'], now=0 , rate=0, ma5=0, ma20=0, ma60=0)
    try:
        tempStock.save(force_insert=True)
        print("addStockCode - Save Stock")
        return HttpResponse("[{\"result\": 1}]")
    except:
        print("addStockCode - Stock already exist")
        return HttpResponse("[{\"result\": 3}]")

def showStockInfo(request):
    print("showStockInfo")
    results = [stock.showStockInfo() for stock in stock.objects.all()]
    return HttpResponse(json.dumps(results, indent=4), content_type="application/json")
