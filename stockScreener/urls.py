from django.conf.urls import url
from django.contrib import admin

#from .views import stockListAPIView

from .views import (
    startStockNow,
    stopStockNow,
    startStockMA,
    addStockCode,
    showStockInfo,
)

urlpatterns = [
    url(r'^startStockNow/$', startStockNow, name='startStockNow'),
    url(r'^stopStockNow/$', stopStockNow, name='stopStockNow'),
    url(r'^startStockMA/$', startStockMA, name='startStockMA'),
    url(r'^addStockCode/$', addStockCode, name='addStockCode'),
    url(r'^showStockInfo/$', showStockInfo, name='showStockInfo'),
    # Examples:
    # url(r'^$', 'openStock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.showlist, name='showlist')
    #url(r'^showlist/', views.showlist, name='showlist')
    #url(r'^stocklist/', stockListAPIView.as_view(), name='stockListView')
]
