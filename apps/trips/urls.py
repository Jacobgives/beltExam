from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [   # This line has changed!
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<id>\d+)$', views.show, name ='show'),
    url(r'^create/$',views.create, name='create'),
    url(r'^createa/$', views.createa, name="createa"),
    url(r'^add/(?P<id>\d+)$',views.add, name="add")
    ]
