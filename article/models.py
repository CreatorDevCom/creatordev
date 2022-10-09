from uuid import uuid4
from django.db import models
from user.models import CustomUser as User
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
  id = models.UUIDField(default=uuid4,  primary_key=True  , null=False , unique=True)
  title = models.CharField(max_length=200)
  author = models.ForeignKey(User,  on_delete=models.CASCADE)
  tags = models.CharField(max_length=50 ,null=True)
  body = RichTextField()
  mainImage = models.ImageField(upload_to='article_mainImages')
  posted_at = models.DateTimeField(auto_now=True)
  views = models.ManyToManyField(User , related_name="article_views")
  likes = models.ManyToManyField(User,related_name='article_likes')

  def count_article_likes(self):
    return self.likes.count()
 
  def count_article_views(self):
    return self.views.count()
 

  def __str__(self):
    return f"{self.title} - By {self.author} - at {self.posted_at}"

class Comment(models.Model):
  id = models.AutoField(primary_key=True , unique=True)
  parent = models.ForeignKey('self',on_delete=models.CASCADE , null=True)
  article = models.ForeignKey(Article ,on_delete=models.CASCADE)
  text = models.TextField(default="")
  author = models.ForeignKey(User , on_delete=models.CASCADE)
  likes = models.ManyToManyField(User , related_name='comment_likes')
  commented_at = models.DateTimeField(auto_now=True)


  def count_comment_likes(self):
    return self.likes.count()

  def __str__(self):
    return f"By {self.author} - at {self.commented_at}"
