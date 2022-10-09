from django.core.mail import send_mail , send_mass_mail 

def send_congrates_new_account_mail(username , email ): 
  try:
    send_mail( 
      subject = "Welcome To Creator Dev!",
      message = f"Hey {username}! welcome ot creator dev. Hope you'r doing well. Grow your skills with us , \n Please verify your email before continue ",
      from_email =  "afnanahad2@gmail.com",
      recipient_list = [email],
      fail_silently=False,
  )
  except ConnectionError as e:
    print(e)
    print("We Can't send you email")


def sendForum_EmailConfiramtionOtp(email):
  numbers = '123456'


