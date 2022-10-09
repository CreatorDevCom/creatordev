from django.urls import path
from home import views

urlpatterns = [
  path("",views.homeRenderer , name='home'), 
]