from django.conf.urls import url
from django.contrib import admin

#from .views import stockListAPIView

from .views import (
    getStockNow,
)

urlpatterns = [
    url(r'^get/$', getStockNow, name='getStockNow'),
    # Examples:
    # url(r'^$', 'openStock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.showlist, name='showlist')
    #url(r'^showlist/', views.showlist, name='showlist')
    #url(r'^stocklist/', stockListAPIView.as_view(), name='stockListView')
]
