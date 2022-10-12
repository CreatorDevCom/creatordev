from http.client import HTTPResponse
from api.send_emails import send_congrates_new_account_mail
from api.models import PrivacyPolices , FeedBack
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect  , Http404
from django.contrib import messages


def sendNewAccountCongrates_Mail(request):
  print("Email sended") 



# Privacy polices
def privacyPolices(request):
  privacy_polices = PrivacyPolices.objects.all()
  # try:
  #   send_congrates_new_account_mail("Afnan ahad" , "mr13ha24ck57er68@gmail.com")
  #   print("email is send")
  # except :
  #    print("Not send")
  context = {"privacy_polices":privacy_polices}

  return render(request,'privacy_polices.html' ,context )



def feedback(request): 
  if request.method == "POST": 
    username = request.POST['username']
    email = request.POST['email'] 
    text = request.POST['text']

    if text and email :
      FeedBack.objects.create(username = username  , email = email , feedtext = text )
      messages.success(request,'Your feedback is submitted success')

  else:
    return redirect("/")