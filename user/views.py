from user.models import UserProfile
from time import time 
from django.contrib.auth.hashers import make_password 
from django.shortcuts import redirect, render
from user.models import CustomUser as User
from django.contrib import messages
from article.models import Article
from user.models import Action, UserProfile
from user.models import Inbox
from django.contrib.auth import login , logout , authenticate 
from api.send_emails import send_congrates_new_account_mail , send_otp_code 
from api.lib import generateOtp
# Create your views here.


# User Profile Preview
def userPofilePreview(request , username):
  user = User.objects.get(username = username)
  user_profile = UserProfile.objects.get(author = user)
  articles = Article.objects.filter(author = user)
  context = {
    "profile":user_profile,
    "articles":articles,
 
  }
  return render(request , 'user/profile.html' , context)



# User Inbox
def userInbox(request):
  if request.user.is_authenticated:
    inbox = Inbox.objects.get(author = request.user)
    actions = Action.objects.filter(to = inbox.author).order_by("-action_at")  
    unreadActions = Action.objects.filter(to = inbox.author , isSeen = False) 
    context ={
      "inbox":inbox,
      "actions":actions,
      "unreadActions":unreadActions
    }
  
    return render(request,"inbox.html" , context)
  else:
    messages.error("Please login first")
    return redirect('/user/login')
  


# User Register
def userRegister(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    c_password = request.POST['c_password'] 
  
    if password == c_password: 
      if len(password) >= 8:
        if User.objects.filter(username = username).exists():    
          messages.error(request,"THis is username is not avaliable")
  
        if User.objects.filter(email = email).exists():    
          messages.error(request,"THis is email is already taken") 
        # try:
        user = User.objects.create(username = username , password = password  , email = email , first_name = first_name , last_name = last_name)
        user.password = make_password(password)
        user.otp = generateOtp(6)
        user.save() 
        print("User registered success") 
        try:
          auth_user = authenticate(request , email = email , password = password)
          if auth_user is not None:
            login(request ,auth_user)  
            return redirect('/')
        except :        
            messages.error(request,"Does't logined ,please try manually")
            print("Does't logined ,please try manually")
            return redirect('/user/login')
        # except :      
        #     messages.error(request,"Error while creating account , Please try again") 
        #     print("Does't registerd")
            
      else:  
        messages.error(request,"Password is less than 8 character")
        
    else:  
      messages.error(request,"Password does't matched")  
      
  return render(request , 'user/register.html')



# Login User
def userLogin(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    if email and password:
      user = authenticate(request , email = email , password = password)
      if user is not None:
        login(request ,user) 
        messages.success(request,f"Welcome ,  you'r login success")
        return redirect('/')
      else:
        messages.error(request,"Username or password doesnot matched")
    else: 
      messages.error(request,"Please fill the form correctly")

  return render(request , 'user/login.html')


# User Logout
def userLogout(request):
  is_authenticated = request.user.is_authenticated
  if is_authenticated:
    logout(request)
    return redirect("/")
  else:
    print("user is not logged in")


# Add Follower
def addFollower(request,username):
  if request.user.is_authenticated:
    article_user = User.objects.get(username = username)
    # Article user profile
    article_user_profile = UserProfile.objects.get(author = article_user)
    try:
      if request.user.is_authenticated:
        # Request user profile ( loged in user)
        req_user_profile = UserProfile.objects.get(author = request.user)
        alreadyFollowing =article_user_profile.followers.filter()
        if req_user_profile.author in alreadyFollowing:
          print("You already followed them")
          messages.success(request,f"You already following  {article_user.first_name} {article_user.last_name}")  
        else:
          article_user_profile.followers.add(request.user)
          print("You started following them")
          req_user_profile.following.add(article_user)
          Action.objects.create(by = request.user , to = article_user ,action = f"Started Following You" , redirect_link=f"#")
          messages.success(request,f"Now you are following {article_user.first_name} {article_user.last_name}") 
      else:
        messages.error(request,"You need to login first")
        return redirect("/user/login")
    except :
        messages.error(request,"Error while attempting request, please try again")
  else:
    messages.warning(request,"Please login first...... to continue")
    return redirect('/user/login')


# Get User by Username
def getUserByusername(request):
  if request.method == "GET":
    data = request.GET['username']
    print(data)


# is Notifaction Seen
def actionSeen(request,id):
  old_action = Action.objects.get(id = id)
  action = Action.objects.filter(id=  id)
  if old_action.isSeen == False:
    action.update(isSeen = True); 
  else:
    pass



# Delete All Actions in inbox
def deleteAllActions(request):
  if request.user.is_authenticated: 
    req_user_inbox_actions = Action.objects.filter(to = request.user).all()
    for i in req_user_inbox_actions:
      i.delete()
    return redirect('/user/inbox')
  else:
    return redirect('/')


# Edit Profile
def profileEdit(request):
  if request.user.is_authenticated:
    profile = UserProfile.objects.filter(author = request.user)
    user = User.objects.filter(username = request.user.username)
    if request.method == 'POST':
      try:  
        # Profile Pic 
        try:
          profile_pic = request.FILES['pro_pic']
          profile.update(profile_pic = profile_pic)
        except:
          pass

        # Cover Pic 
        try:
          cover_pic = request.FILES['cover_pic']
          profile.update(cover_pic = cover_pic) 
        except :
          pass

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        bio = request.POST['bio']


          # First Name
        if first_name:
          user.update(first_name = first_name) 
          
          # Last Name
        if last_name:
          user.update(last_name = last_name) 

          # Bio
        if bio:
          profile.update(bio = bio) 
          
        messages.success(request  ,"Profile has been updated")
        return redirect("/user/editprofile/edit")
      except :
        messages.success(request  ,"Error Occured while updating profile") 
   
    context = {
      "user":user,
      "profile":profile,
    }
    return render(request,"user/profile_edit.html" , context)
  else:
    messages.error(request,'Please login First')
    return redirect("/user/login")




# Email varifaction (otp)
def veifyEmail(request):
  if request.user.is_authenticated:
    if not request.user.is_em_verified:
      # send an otp code
      username = request.user.username
      email =  request.user.email 
      user = User.objects.filter(username = username) 
      saved_opt = ''
      # otp code saved in user
      for i in user: 
        saved_opt = str(i.otp) 

      try:
        send_otp_code( username,email,saved_opt )
        print('email is sended')
      except ConnectionError as e:
        print('hi')

  
      if request.method == "POST": 
          code1 = request.POST['otp-code-1']
          code2 = request.POST['otp-code-2']
          code3 = request.POST['otp-code-3']
          code4 = request.POST['otp-code-4']
          code5 = request.POST['otp-code-5']
          code6 = request.POST['otp-code-6']
          
          # Otp code from user input
          otpCode = str(code1+""+code2+""+code3+""+code4+""+code5+""+code6) 


      
          if saved_opt == otpCode:
            user.update(is_em_verified = True)
            messages.success(request,"Your email has been verified")
          else:
            messages.error(request,"Otp not matched")

      return render(request,"user/email_verify.html")

    return redirect("/")
  return redirect("/")

 
 