from django.contrib import admin
from blogapp import models

admin.site.register([
  models.BlogModel
])