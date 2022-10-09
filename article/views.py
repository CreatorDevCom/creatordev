from email import message
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from article.lib import isFollowing  
from user.models import Action, UserProfile
from django.contrib import messages
from .models import Article , Comment
from user.models import CustomUser as User
from django.contrib.auth.models import AnonymousUser
from django.forms import forms
from django.core.paginator import Paginator
from forum.models import Forum
# Create your views here. 


def articleIndex(request):
  allarticles = Article.objects.all().order_by('-posted_at')
  # Get only 12 article for one page
  getarticles = Paginator(allarticles,12)
  # Get pagenumber from request
  page_number = request.GET.get("page")
  articles = getarticles.get_page(page_number)
  
  # User Profile
  userprofile= []
  for i in articles:
    author = i.author 
    userprofile = UserProfile.objects.filter( author = author)     
  
  # Chech Next page
  current_page = 1
  next_next_page_number = current_page + 2
  if page_number is not None:
    current_page = page_number

  # Check if request.user following the article user
   

  context={
    "articles":articles, 
    "userprofile":userprofile, 
    "current_page":current_page  ,
    "next_next_page_number":next_next_page_number  ,
  }
  return render(request ,'article/index.html' , context)

def previewArticle(request , id):
  article = Article.objects.get(id = id)
  profile = UserProfile.objects.get(author = article.author)    
  followers = profile.followers.all() 
  
  comments = Comment.objects.filter(article = article , parent=None)
  replies = Comment.objects.filter(article = article).exclude(parent=None)
  repDict = {}   
  # Increase 1 view on visit
  if request.user.is_authenticated:
    article.views.add(request.user) 
 
  # Reply of/to comment
  for reply in replies: 
    if reply.parent.id not in repDict.keys():
      repDict[reply.parent.id] = [reply]
    else:
      repDict[reply.parent.id].append(reply) 


  isfollowing = isFollowing(request , followers) 
  context={
  "article":article,
  "profile":profile,
  "comments":comments,
  "isFollowing":isfollowing,
  "reply":repDict, 
  }
  return render(request , 'article/preview.html' , context)


def createNew(request):
  if request.user.is_authenticated:
    
    if request.method == "POST":

      title = request.POST['title']
      tags = request.POST['tags']
      articleBody = request.POST['article-body']
      mainImage = request.FILES['main-image']

      userProfile = UserProfile.objects.get(author = request.user)  

      following = userProfile.following.all() 
      
      if title and mainImage and articleBody:
        # try:
          article = Article.objects.create( title = title , author = request.user ,tags = tags , body = articleBody , mainImage = mainImage )
          for user_b in following:
            Action.objects.create(by = request.user , to = user_b ,action = f"Create New Article , you are following him" , redirect_link=f"/article/{article.id}")

          messages.success(request,"Your article has been Uploaded")
          return redirect("/article")
        # except:
          # messages.error(request , "Does't create an article")
      else:
        messages.error(request , "please fill the form correctly")
            

    return render(request , 'upload/createnew.html' )
  else:
    messages.warning(request,"Please login first to create new article")
    return redirect('/user/login')



def ckEditor(request):
  return render(request , 'ckeditor/index.html')


def searchArticle(request):
  if request.method == "GET":
    query = request.GET['q'] 
    query = query.lower()
    title_contains = Article.objects.filter(title__icontains = query)
    tags_contains = Article.objects.filter(tags__icontains = query)
    articles = tags_contains.union(title_contains)

    # Get only 12 article for one page
    getarticles = Paginator(articles,12)
    # Get pagenumber from request
    page_number = request.GET.get("page")
    articles = getarticles.get_page(page_number)

    current_page = 1 
    if page_number is not None:
      current_page = page_number
      
    context ={
      "query":query,
      "articles":articles,
      "current_page":current_page,
    }
    return render(request , 'search.html',context)
  return render(request , 'search.html')

def likeArticle(request,article_id):
  if request.user.is_authenticated: 
    try:
      article = Article.objects.get(id = article_id)
      already_liked = article.likes.filter()
      if request.user in already_liked:
        print("Already Liked")
      else:
        article.likes.add(request.user)
        Action.objects.create(by = request.user , to = article.author ,action = f"Like your post ' {article.title[0:25]} ' " , redirect_link=f"/article/{article.id}")
        messages.success(request,"You like this article")
        return redirect(f'/article/{article_id}')
    except : 
      messages.success(request,"Can't liked article")
      print("Error occured")
      return redirect(f'/article/{article_id}')
  else:
    messages.error(request,  "please login first")
 
def postAComment(request,id):
  if request.method == 'POST':
    if request.user.is_authenticated:
      text = request.POST['comment-text']
      try:
        on_article = Article.objects.get(id = id)
        comment = Comment.objects.create(article = on_article , author = request.user , text=text)
        Action.objects.create(by = request.user , to = on_article.author ,action=f"Comment on your post '{text}'" , redirect_link =f"/article/{on_article.id}#{comment.id}")
        messages.success(request,"Comment is been submitted") 
        return redirect(f'/article/{on_article.id}')
      except:
         messages.error(request ,"Does't post a comment ")
         return redirect(f'/article/{on_article.id}')
    else:
      messages.error(request,"Login required to post a comment")
      return redirect('/user/login')
  else:
    messages.error(request,"Method not allowed") 
    return redirect("/")

# Like a Comment
def likeComment(request,commentId):
  if request.user.is_authenticated: 
    try:
      comment = Comment.objects.get(id = commentId)
      already_like = comment.likes.filter()

      if request.user in already_like:
        messages.success(request,"Your have already liked !!")
      else:
        comment.likes.add(request.user) 
        Action.objects.create(by = request.user , to = comment.author ,action = f"Like your comment ' {comment.text[0:25]} ' " , redirect_link="#")
        messages.success(request,"You like a comment")  
    except : 
      print("You can't liked a comment") 
  else:
    messages.error(request,  "please login first")
 


def sendReplay(request,id):
  if request.method == 'POST':
    if request.user.is_authenticated:
      article_id = request.POST['article-id']
      text = request.POST['replay-text']
      try: 
        on_article = Article.objects.get(id = article_id)
        on_comment = Comment.objects.get(id = id)
        Comment.objects.create(article = on_article,author = request.user , text=text , parent = on_comment )
        Action.objects.create(by = request.user , to = on_comment.author ,action=f"Reply on your comment '{text}'" , redirect_link=f"/article/{on_article.id}#{on_comment.id}")
        messages.success(request,"replay is been submitted")
        return redirect(f"/article/{on_article.id}") 
      except:
         messages.error(request ,"Does't post a comment ")
         return redirect(f"/article/{on_article.id}")
    else:
      messages.error(request,"Login required to post a comment")
      return redirect('/user/login')
  else:
    messages.error(request,"Method not allowed") 
    return redirect("/")


# Get Article for a specific user
def getArticleForASpecificUser(request , username):
  user = User.objects.get(username = username)
  articles = Article.objects.filter(author = user)
  comments = Comment.objects.filter(article = articles)
  context = {
    "articles":articles,
    "comments":comments
  }
 
  return context


# Edit Article
def editArticle(request,id):
  if request.user.is_authenticated:
    if Article.objects.filter(id = id).exists():
      old_article = Article.objects.get(id = id)

      if request.method == "POST": 
        title = request.POST['title']
        tags = request.POST['tags']
        articleBody = request.POST['article-body']  
        try: 
          article = Article.objects.filter(id = id)
          article.update(title = title , tags = tags , body = articleBody )
          messages.success(request,"Your article has been edited")
          return redirect(f"/article/{old_article.id}")
        except :
            pass

      context = {"old_article":old_article}
      return render(request,"upload/edit_article.html",context)
    else:
      return redirect('/404.html')
