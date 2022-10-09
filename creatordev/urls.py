from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from api.views import privacyPolices
urlpatterns = [
    path("account/", include("allauth.urls")),
    path('admin/', admin.site.urls),  
    path("api/",include("api.urls")), 
    path("",include("home.urls")),
    path("article/",include("article.urls")), 
    path("forum/",include("forum.urls")), 
    path("user/",include("user.urls")),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
