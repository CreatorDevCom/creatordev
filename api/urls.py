from django.urls import path
from api import views


urlpatterns=[
  path('privacy_polices/',views.privacyPolices , name='privacy_polices' ),
  path('send_email',views.sendNewAccountCongrates_Mail,name="new_account_congrates_main"),  
  path('feedback',views.feedback , name='feedback' ),
]