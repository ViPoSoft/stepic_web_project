from django.conf.urls import patterns, include, url
#from django.contrib import admin
#from . import views
from qa.views import test

urlpatterns = patterns('',
    url(r'^$', test, name='test'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/\d+/', test, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
)
#urlpatterns = [
    ## druga sproba
    #url(r'^$', views.test, name='test'), 
    #url(r'^login/.*$', views.test),
    #url(r'^signup/.*$', views.test),
    #url(r'^ask/.*$', views.test),
    #url(r'^popular/.*$', views.test),
    #url(r'^new/.*$', views.test),
    #url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
#]	
