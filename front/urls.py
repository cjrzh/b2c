
from django.conf.urls import url

from front import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]