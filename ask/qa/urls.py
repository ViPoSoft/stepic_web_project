from django.conf.urls import patterns, include, url
#from django.contrib import admin
#from . import views
from django.conf.urls import url
from qa.views import question

urlpatterns = [
    url(r'^(?P<num>\d+)/$', question),
]
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
