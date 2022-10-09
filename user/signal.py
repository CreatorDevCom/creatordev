from user.models import CustomUser as User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import UserProfile 
from .models import Inbox
from api.send_emails import send_congrates_new_account_mail


# Create Profile for specific User
@receiver(post_save , sender = User)
def create_profile(sender , instance , created , **kwargs):
  if created:
    userProfile = UserProfile.objects.create(author = instance , stars = 0 ,  )
    userProfile.save()
 

# Create Inbox for specific User
@receiver(post_save , sender = User)
def create_inbox(sender , instance , created , **kwargs):
  if created:
    userinbox = Inbox.objects.create(author = instance )
    userinbox.save()
 
 