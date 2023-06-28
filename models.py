from django.db import models

from ckeditor.fields import RichTextField

class Post(models.Model):
    body=RichTextField(blank=True,null=True)