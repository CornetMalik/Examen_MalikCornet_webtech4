from django.conf.urls import url, include
from eightball import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^start', views.start,name='start'),
]