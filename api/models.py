from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class PrivacyPolices(models.Model):
  text = RichTextField()
  updated_on = models.DateTimeField(auto_now = True)


class FeedBack(models.Model):
  id = models.AutoField(primary_key=True  , unique  = True)
  username = models.CharField(max_length=20 , blank = True) 
  email = models.EmailField(max_length=50 , blank = True)
  feedtext = models.TextField(blank = True )
  created_at = models.DateTimeField(auto_now = True)