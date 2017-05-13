from django.shortcuts import render
from .models import stock
import time

# Create your tests here.

while(1) :
    time.sleep(60)
    print("getstock")
    for stock in stock.objects.all() :
        stock.checkNow()

"""
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
