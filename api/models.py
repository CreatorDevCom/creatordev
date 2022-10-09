from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class PrivacyPolices(models.Model):
  text = RichTextField()
  updated_on = models.DateTimeField(auto_now = True)
