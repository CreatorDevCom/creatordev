from django.urls import path
from home import views

urlpatterns = [
  path("",views.homeRenderer , name='home'), 
  path("upload",views.upload , name='upload'), 
  path("search/",views.search , name='search'), 
  path("404",views.notfound404 , name='404'), 
]