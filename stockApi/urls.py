from django.conf.urls import url
from django.contrib import admin

from .views import (
#  itemCreateAPIView,
#  itemListAPIView,
  parsingJson,
  showlist,
)


urlpatterns = [
    # Examples:
    # url(r'^$', 'openStock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.showlist, name='showlist')
    url(r'^create/$', parsingJson, name='create'),
    url(r'^list/$', showlist, name='create'),

    #url(r'^list1/', itemListAPIView.as_view(), name='list'),
    #http://127.0.0.1:8000/stockApi/create/?JSON={"title":"123","url":"321http//www.naver.com","stockNum":3,"stock1Code":"053800","stock2Code":"005930","stock3Code":""}
]
