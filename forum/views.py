from django.shortcuts import render , redirect
from django.contrib import messages

from article.lib import isFollowing 
from forum.models import Forum   , Comment 
from user.models import Action, UserProfile

# Forum Index Page (Home Page)
def forumIndex(request):

  # Get All Forums
  forums = Forum.objects.all().order_by('-pk') 
   
  # Get Forum User Profile
  userprofile= []
  for i in forums:
    author = i.author 
    userprofile = UserProfile.objects.get( author = author)     
  
  context = {
    "forums":forums, 
    "userprofile":userprofile,
  }

  return render(request,'forum/forum_index.html',context)



def forumPreview(request,id):
  if Forum.objects.filter(id = id).exists():
    forum = Forum.objects.get(id = id)  
    profile = UserProfile.objects.get(author = forum.author)   
    followers = profile.followers.all() 
    comments = Comment.objects.filter(forum = forum , parent=None)
    replies = Comment.objects.filter(forum = forum).exclude(parent=None)
    repDict = {}    
    isfollowing = isFollowing(request , followers)   
    
  
 
  # Reply of/to comment
  for reply in replies: 
    if reply.parent.id not in repDict.keys():
      repDict[reply.parent.id] = [reply]
    else:
      repDict[reply.parent.id].append(reply) 


  context = {
    "forum":forum, 
    "comments":comments,
    "isFollowing":isfollowing,
    "profile":profile,
    "reply":repDict,
  }


  return render(request , "forum/forum_preview.html" , context)


def createAComment(request,id):
  if request.method == 'POST':
    if request.user.is_authenticated:
      text = request.POST['comment-text']
      
      # Check is  forum is Guest or not
      if Forum.objects.filter(id = id).exists():
        on_forum = Forum.objects.get(id = id)
        comment = Comment.objects.create(forum = on_forum , author = request.user , text=text)
        Action.objects.create(by = request.user , to = on_forum.author ,action=f"Comment on your forum '{text[0:30]}'" , redirect_link =f"/forum/preview/{on_forum.id}#{comment.id}")
        messages.success(request,"Comment is been submitted") 
        return redirect(f'/forum/preview/{on_forum.id}') 
 
        

      
    else:
      messages.error(request,"Login required to post a comment")
      return redirect('/user/login')
  else:
    messages.error(request,"Method not allowed") 
    return redirect("/")


# Send reply
def sendReply(request,id):
  if request.method == 'POST':
    if request.user.is_authenticated: 
      text = request.POST['replay-text']  
      forum_id = request.POST['forum-id']
      # Check is not Guest Forum
      if Forum.objects.filter(id = forum_id).exists():
        on_forum = Forum.objects.get(id = forum_id)
        on_comment = Comment.objects.get(id = id)
        Action.objects.create(by = request.user , to = on_comment.author ,action=f"Reply on your comment '{text[0:30]}'" , redirect_link=f"/forum/preview/{on_forum.id}#{on_comment.id}")
        Comment.objects.create(forum = on_forum,author = request.user , text=text , parent = on_comment )
        messages.success(request,"replay is been submitted")
        return redirect(f"/forum/preview/{on_forum.id}") 
 
 
    else:
      messages.error(request,"Login required to post a comment")
      return redirect('/user/login')
  else:
    messages.error(request,"Method not allowed") 
    return redirect("/")


# Like a comment
def likeComment(request,id):
  if request.user.is_authenticated: 
    try:
      comment = None
      if Comment.objects.filter(id = id).exists():
        comment = Comment.objects.get(id = id) 
      
      already_like = comment.likes.filter() 
      if request.user in already_like:
        messages.success(request,f"Aleady Like a comment {comment.id}") 
      else:
        comment.likes.add(request.user) 
        Action.objects.create(by = request.user , to = comment.author ,action = f"Like your comment ' {comment.text[0:25]} ' " , redirect_link="/user/inbox/#")
        messages.success(request,"You like a comment")  
    except : 
      print("You can't liked a comment") 
  else:
    messages.error(request,  "please login first")
 
# Upload forum
def uploadForum(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      title = request.POST['title']
      body = request.POST['body'] 

      userProfile = UserProfile.objects.get(author = request.user)  
      following = userProfile.following.all() 
      try:

        
        if title and body:
          # try:
            forum = Forum.objects.create( title = title , author = request.user  , body = body)
            for user_b in following:
              Action.objects.create(by = request.user , to = user_b ,action = f"Post a Forum , you are following him" , redirect_link=f"/forum/preview/{forum.id}")
            messages.success(request,"Your forum has been upload")
            return redirect("/forum")

      except ValueError :
          messages.error(request,"Error while creating Forum , please try again")

  return render(request,'upload/upload_forum.html')


# Like Forum
def likeForum(request,id):
  # Chech is user is authenticated
  if request.user.is_authenticated:  
    # Check if  forum is not GUEST DO
    if Forum.objects.filter(id = id).exists():
      forum = Forum.objects.get(id = id) 
      already_like = forum.likes.filter() 

      # Check user likes this forum??
      if request.user in already_like:
        pass
      else:
        try:
          # Add Like of request user
            forum.likes.add(request.user)
            messages.success(request,"You Liked this forum") 
            Action.objects.create(by = request.user , to = forum.author ,action = f"Like your forum ' {forum.title[0:25]} ' " , redirect_link=f"/forum/preview/{forum.id}")
            return redirect(f"/forum/preview/{forum.id}")
        except : 
            messages.error(request,"You Does't Like this forum") 
  else:
    messages.error(request,"To like forum you will need for Login first")


 



# Edit forum 
def eidtForum(request , id): 
  if request.user.is_authenticated: 
    if Forum.objects.filter(id = id).exists():  
      old_forum  = Forum.objects.get(id = id)
      if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']  
        try: 
          if title and body: 
            forum = Forum.objects.filter(id = id)
            forum.update(title = title , body = body )
            messages.success(request,"Your Forum has been Edit")
            return redirect(f"/forum/preview/{old_forum.id}")   
        except ValueError :
            messages.error(request,"Error while Editing Forum , please try again")
    else:
      messages.info(request,"not found")


    context={
      "old_forum":old_forum,
    }
    return render(request,'upload/edit_forum.html',context)
  else:
    messages.warning(request,"Only registered user able to do this")
    return redirect('/user/login')


