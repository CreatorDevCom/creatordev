from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from article.models import Article 
from user.manager import UserManager

# Custom User
class CustomUser(AbstractUser): 
  username = models.CharField(max_length=50,default="",unique=True,blank=True) 
  email = models.EmailField(unique=True)
  is_em_verified = models.BooleanField(default=False)
  phone = models.CharField(max_length=20)
  email_token = models.CharField(max_length=100 , null=True ,blank=True)
  forget_password = models.CharField(max_length=100,null=True , blank=True)
  last_login_time = models.DateTimeField(null=True , blank=True)
  last_logout_time = models.DateTimeField(null=True , blank=True)
  otp = models.IntegerField(unique = True,null = True , blank = True)
  objects = UserManager()

  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = ['username' ]


# User Profile
class UserProfile(models.Model):  
  id = models.AutoField(null=False,unique=True,primary_key=True)
  author = models.OneToOneField(CustomUser , on_delete=models.CASCADE  ,related_name='user_profile')
  profile_pic = models.ImageField(default="user/default/default_profile.jpg",  upload_to='user/profile_pic')
  cover_pic = models.ImageField(default="user/default/default_cover.jpg",  upload_to='user/cover_pic')
  followers = models.ManyToManyField(CustomUser, related_name='followers')
  following = models.ManyToManyField(CustomUser, related_name='following')
  bio = models.TextField(default=f"Hey! I have an experience to create or write helpfull articles")
  stars = models.IntegerField()

  def Stars(self):
    stars = self.stars
    # article = Article.objects.filter(author = self.author)
    # for i in article: 
    #   stars += i.likes.count()
    return stars

  def count_followers(self):
    return self.followers.count()

  def count_following(self):
    return self.following.count()

  def __str__(self):
    return f"{self.author} , followers - {self.count_followers()} , stars - {self.stars}"


# Actions 
class Action(models.Model):
  id = models.UUIDField(default=uuid4 , null=False , unique=True , primary_key=True)
  by = models.ForeignKey(CustomUser , on_delete=models.CASCADE ,related_name="user_by")
  to = models.ForeignKey(CustomUser , on_delete=models.CASCADE ,related_name="user_to")
  action = models.CharField(max_length=200)
  redirect_link = models.CharField(max_length=100 ,default="")
  isSeen = models.BooleanField(default=False)
  action_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.by} {self.action}"

# Inbox
class Inbox(models.Model):
  id = models.AutoField(primary_key=True,  null= False , unique=True)
  author = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name="user_inbox")
  actions = models.ManyToManyField(Action , related_name="actions")

  def __str__(self):
    return self.author.username

  def count_actions(self):
    return self.actions.count()