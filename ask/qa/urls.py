#from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<question_id>[0-9]+)/$', views.test, name='test'),
]	
