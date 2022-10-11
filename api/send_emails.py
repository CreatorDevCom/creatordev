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


 

def send_otp_code(username,email,otp):
  try:
    send_mail( 
      subject = "Verify email address",
      message = f"Hi {username} ! \nYour email varification code is \n <h1> {otp}</h1> ",
      from_email =  "creatordevcommunity@gmail.com",
      recipient_list = [email],
      fail_silently=False,
    )
  except ConnectionError as e:
    print(e)
    print("We Can't send you email")
