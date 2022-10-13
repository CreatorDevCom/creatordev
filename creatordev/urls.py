from django.contrib import admin
from django.urls import path , include  
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import re_path as url
from api.views import privacyPolices
from django.views.static import serve
urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),  
    path("api/",include("api.urls")), 
    path("",include("home.urls")),
    path("article/",include("article.urls")), 
    path("forum/",include("forum.urls")), 
    path("user/",include("user.urls")),  
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT})
url(r'^static/(?P<path>.*)$',serve,{"document_root":settings.STATIC_ROOT})