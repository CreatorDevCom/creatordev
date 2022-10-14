import uuid
from django.db import models
from user.models  import CustomUser as User
from ckeditor.fields import RichTextField

# Create your models here.
class Forum(models.Model):
  id= models.AutoField(primary_key = True , null=False)
  author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="forum_author")
  title = models.CharField(max_length=400 )
  body = RichTextField()
  posted_at = models.DateTimeField(auto_now=True) 
  likes = models.ManyToManyField(User , related_name="forum_likes")

  def count_forum_likes(self):
    return self.likes.count()

  def __str__(self):
    return f'{self.title} - by - {self.author}'

class GuestForum(models.Model):
  id = models.UUIDField( default=uuid.uuid4(), primary_key=True  , null=False  )
  author = models.CharField(max_length=50)
  email = models.EmailField(max_length=150)
  title = models.CharField(max_length=400)
  body = RichTextField()
  posted_at = models.DateTimeField(auto_now=True) 
  likes = models.ManyToManyField(User , related_name="guest_forum_likes")

  def count_forum_likes(self):
    return self.likes.count()

  def __str__(self):
    return f'{self.title} - by - {self.author}'

class Comment(models.Model):
  id = models.AutoField(primary_key=True , unique=True)
  parent = models.ForeignKey('self',on_delete=models.CASCADE , null=True)
  forum = models.ForeignKey(Forum ,on_delete=models.CASCADE)
  text = models.TextField(default="")
  author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="forum_comment_author")
  likes = models.ManyToManyField(User , related_name='forum_comment_likes')
  commented_at = models.DateTimeField(auto_now=True)
  
  def count_comment_likes(self):
    return self.likes.count()

  def __str__(self):
    return f"By {self.author} - at {self.commented_at} - id {self.id}"

class GuestForumComment(models.Model):
  id = models.UUIDField(default=uuid.uuid4(),primary_key=True )
  parent = models.ForeignKey('self',on_delete=models.CASCADE , null=True)
  forum = models.ForeignKey(GuestForum ,on_delete=models.CASCADE)
  text = models.TextField(default="")
  author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="guest_forum_comment_author")
  likes = models.ManyToManyField(User , related_name='guest_forum_comment_likes')
  commented_at = models.DateTimeField(auto_now=True)


  def count_comment_likes(self):
    return self.likes.count()

  def __str__(self):
    return f"By {self.author} - at {self.commented_at} - id {self.id}"
