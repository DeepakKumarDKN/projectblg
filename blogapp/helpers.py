from django.utils.text import slugify
from blogapp import models
import random
import string

def generate_random_string(N):
  res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
  return res
 


def generate_slug(text):
  new_slug = slugify(text)
  
  #here i am checking if the slug exists or nor if it doesnot exist then it will return the new slug and if it exists generate the newslug
  if models.BlogModel.objects.filter(slug=new_slug).first():
    return generate_slug(text + generate_random_string(5))
  return new_slug
