from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from blogapp import helpers

class BlogModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = FroalaField()
  slug = models.SlugField(max_length=100, null=True, blank=True)
  image = models.ImageField(upload_to="blog")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
  #overriding the save method
  def save(self, *args, **kwargs):
    self.slug = helpers.generate_slug(self.title)
    super(BlogModel, self).save(*args,**kwargs)
  