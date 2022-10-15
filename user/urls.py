from django.urls import path
from user import views
urlpatterns= [
  path('inbox',views.userInbox , name="inbox"),
  path('email_verification',views.veifyEmail , name="verify_email"),
  path('email_verification/resend_otp',views.re_send_otp , name="re_send_otp"),
  path('inbox/clearall',views.deleteAllActions , name="clearall"),
  path('register',views.userRegister , name="register"),
  path('login',views.userLogin , name="login"),
  path('logout',views.userLogout , name="logout"),
  path('editprofile/edit',views.profileEdit , name="profileedit"),
  path('actionseen/<str:id>',views.actionSeen , name="actionseen"),
  path('addfollower/<str:username>',views.addFollower , name="addfollower"),
  path('profile/<str:username>',views.userPofilePreview,name='userprofilepreview'),
]