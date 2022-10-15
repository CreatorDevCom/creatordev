from django.core.mail import send_mail , send_mass_mail  

def send_congrates_new_account_mail(username , email ): 
  try:
    send_mail( 
      subject = "Welcome To Creator Dev!",
      message = f"Hey {username}! welcome to Creator Dev. Hope you'r doing well. Grow your skills with us , \n \n and explore more Knowledge , by reading helpful articles \n \n Knowledge is powerful weapon",
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
      message = f"Hi {username} ! \nYour email varification code is \n   \n{otp} \n Please enter the virification code and You will redirect to home page of Creator Dev   ",
      from_email =  "creatordevcommunity@gmail.com",
      recipient_list = [email],
      fail_silently=False,
    )
  except ConnectionError as e:
    print(e)
    print("We Can't send you email")
