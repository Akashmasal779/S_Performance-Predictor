from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('help', views.help, name='help'),
    path('predict', views.predict_view, name='predict'),
]