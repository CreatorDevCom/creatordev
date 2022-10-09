from forum.models import GuestForum

# Chech Guest forum < 5 than upload
def isAbleToUpload(guestForumemail):
  if GuestForum.objects.filter(email = guestForumemail).exists(): 
    guestForums = GuestForum.objects.filter(email = guestForumemail).all() 

    if len(guestForums) < 5:
      return True
    else:
      return False
  else:
    return True

 

