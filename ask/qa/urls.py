#from django.conf.urls import patterns, include, url
from django.conf.urls import  url
from . import views

urlpatterns = [
    ##Examples:
    #url(r'^$', views.index, name='index'),
    #url(r'^popular/.*$', views.popular, name='popular'),    
    url(r'^ask/.*$', views.test),
    #url(r'^answer/.*$', views.answer, name='answer'),
    #url(r'^signup/.*$', views.user_signup, name='signup'),
    #url(r'^login/.*$', views.user_login, name='login'),
    #url(r'^logout/.*$', views.user_logout, name='logout'),    
    #url(r'^new/.*$', views.test), 
    ## url(r'^$', 'ask.views.home', name='home'),
    ## url(r'^blog/', include('blog.urls')),
    url(r'^(?P<question_id>[0-9]+)/$', views.test),
]	
