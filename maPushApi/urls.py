from django.conf.urls import url
from django.contrib import admin

from .views import (
  addStockCode,
  showStockInfo,
)


urlpatterns = [
    url(r'^addStockCode/$', addStockCode, name='addStockCode'),
    url(r'^showStockInfo/$', showStockInfo, name='showStockInfo'),
]
