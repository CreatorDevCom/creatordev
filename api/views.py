from api.send_emails import send_congrates_new_account_mail
from api.models import PrivacyPolices
from django.shortcuts import redirect, render



def sendNewAccountCongrates_Mail(request):
  print("Email sended") 



# Privacy polices
def privacyPolices(request):
  privacy_polices = PrivacyPolices.objects.all()
  try:
    send_congrates_new_account_mail("Afnan ahad" , "mr13ha24ck57er68@gmail.com")
    print("email is send")
  except :
     print("Not send")
  context = {"privacy_polices":privacy_polices}

  return render(request,'privacy_polices.html' ,context )
