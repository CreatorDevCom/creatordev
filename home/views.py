from django.shortcuts import render
from article.models import Article
from forum.models import Forum  
# Create your views here.
def homeRenderer(request):
  return render(request , "index.html")


# Uplaods
def upload(request):
  return render(request,'upload/index.html')


# Search
def search(request):
  if request.method == "GET":
    text = request.GET.get('text')
    text = text.lower()

    # articles 
    articles = Article.objects.filter(title__icontains = text )
    forums = Forum.objects.filter(title__icontains = text ) 

    context= {
      "articles":articles,
      "forums":forums, 
      "text":text,
    }

    return render(request,'search.html',context) 

  
  return render(request,'search.html')


# Not Found 404
def notfound404(request):
  return render(request,'404.html')



