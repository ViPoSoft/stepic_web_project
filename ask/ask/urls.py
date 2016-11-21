#from django.conf.urls import patterns, include, url
django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
from ask import views

urlpatterns = [
    url(r'^$', 'views.ktotam'),
    url(r'^login/', 'views.ktotam'),
    url(r'^signup/', 'views.ktotam'),
    url(r'^ask/', 'views.ktotam'),
    url(r'^popular/', 'views.ktotam'),
    url(r'^new/', 'views.ktotam'),
    url(r'^question/', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', 'views.'views.nicogodomanet'),                   
}
