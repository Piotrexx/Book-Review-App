from django.core.exceptions import ValidationError
from django import forms
from .models import *



class SeachForm(forms.Form):
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
   

class UploadForm(forms.ModelForm):
   class Meta:
      model = MediaModel
      fields = "__all__"
   