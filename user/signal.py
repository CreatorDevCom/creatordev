from user.models import CustomUser as User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import UserProfile 
from .models import Inbox
from api.send_emails import send_congrates_new_account_mail
from api.lib import generateOtp


# Create Profile for new User
@receiver(post_save , sender = User)
def create_profile(sender , instance , created , **kwargs):
  if created:

    # Create profile
    userProfile = UserProfile.objects.create(author = instance)
    userProfile.save()

    # generate otp 
    user = User.objects.get(username = instance.username, stars =0)
    user.ganarate_otp()

    # Send congrates email
    send_congrates_new_account_mail(username = instance.username , email = instance.email)
 

# Create Inbox for new User
@receiver(post_save , sender = User)
def create_inbox(sender , instance , created , **kwargs):
  if created:
    userinbox = Inbox.objects.create(author = instance )
    userinbox.save()
 

 
 