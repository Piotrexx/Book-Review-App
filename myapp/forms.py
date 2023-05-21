from django.core.exceptions import ValidationError
from django import forms
from .models import Book, Publisher, Review

# BOOK_CHOICES = [(Book.objects.order_by('id'))]

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
   
   # def clean(self):
   #    cleaned_data = super().clean()
   #    rating = cleaned_data("rating",0)
   #    if rating > 10:
   #       self.add_errors("rating", "ocdawpihjdapwdawopdghg")
   #    else:
   #       self.add_error(None, "KAKAHJIPHADHIADN")
   #       # raise ValidationError("ocena może być jedynie wystawiona od 0 do 10 !")
   