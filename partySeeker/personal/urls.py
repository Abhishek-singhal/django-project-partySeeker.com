from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about-us/', views.about, name='about'),
    url(r'^index/',views.party, name='party'),
    #url(r'^Agra/$',views.party, name='party'),
]