from django.shortcuts import render
from .models import stock
import time
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Create your tests here.

def getStockNow(request):
    
    gs = web.DataReader("025620.KQ", "yahoo", datetime(2017, 5, 1), datetime(2017, 5, 17))
    print(gs.tail())

"""
    while(1) :
        time.sleep(5)
        print("getstock")
        for stocktemp in stock.objects.all() :
            stocktemp.checkNow()
"""
"""
def getStockMA5(request):
    

from rest_framework.generics import ListAPIView

from stockScreener.models import stock
from stockScreener.serializers import stockSerializer


class stockListAPIView(ListAPIView):
    queryset = stock.objects.all()
    serializer_class = stockSerializer

    def get(self, request, *args, **kwargs):
      print(kwargs)
      return self.retrieve(request, *args, **kwargs)
"""

# Create your views here.
