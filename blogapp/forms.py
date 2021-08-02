from django import forms
from froala_editor.widgets import FroalaEditor
from blogapp import models

class Blogform(forms.ModelForm):
  class Meta:
    model = models.BlogModel
    fields = ['content']