from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'openStock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kakaoApi/', include('kakaoApi.urls')),
    url(r'^stockApi/', include('stockApi.urls')),
    url(r'^stockScreener/', include('stockScreener.urls')),
]
