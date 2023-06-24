from django.core.exceptions import ValidationError
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
   search = forms.CharField(required=False)

class PublisherForm(forms.ModelForm):
   class Meta:
      model = Publisher
      fields = "__all__"

class ReviewsForm(forms.ModelForm):
   rating = forms.IntegerField(max_value=10,min_value=0)
   
   class Meta:
      model = Review
      exclude = ["date_edited", "book"]

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.form_method = "post"
      self.helper.add_input(Submit("", "Search"))

class UploadForm(forms.ModelForm):
   class Meta:
      model = MediaModel
      fields = "__all__"
   