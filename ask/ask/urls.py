#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
from ask import views

urlpatterns = [
    url(r'^', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
]
