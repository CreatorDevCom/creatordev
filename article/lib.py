def isFollowing(request , followers):
    isFollowing = False 
    for i in followers:   
      if request.user.username in i.username:  
        isFollowing = True     

    return isFollowing