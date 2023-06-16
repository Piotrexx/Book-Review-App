from django.db import models
from django.contrib import auth
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.contrib.admin import ModelAdmin

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="nazwa wydawnictwa")

    website = models.URLField(help_text="witryna wydawnictwa")

    email = models.EmailField(help_text="adres email wydawnictwa")

    def __str__(self): # this function is needed to show name in Django admin panel 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=70, help_text="tytuł książki")
    publication_date = models.DateField(verbose_name="Data publikacji książki")
    isbn = models.CharField(max_length=20,verbose_name="number ISBN książki")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # publisher is using ForeignKey that is a many-to-one relationship. Field "publisher" is linked to Publisher Model and if the publisher that is linked to this field will be deleted this will be deleted too. 
    contributors = models.ManyToManyField('Contributor',through="BookContributor")



    def __str__(self):
        return "{} ({})".format(self.title, self.isbn) # it is for showing name and isbn number in Django Admin Panel
    
class Contributor(models.Model):

    first_names = models.CharField(max_length=50, help_text="Imię lub imiona wspołtwórcy")
    last_names = models.CharField(max_length=50, help_text="Nazwizko lub nazwiska współtwórcy")
    email = models.EmailField(help_text="email współtwórcy")
    def number_contributions(self): # count the number of contributors
        return self.bookcontributor_set.count()

    def __str__(self):
        return self.first_names
    

class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        # these are the choices that the Contributor can be
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Rola, jaką współtwórca odegrał podczas tworzenia tej książki.", choices=ContributorRole.choices, max_length=20)

    
class Review(models.Model):
    content = models.TextField(help_text="tekst recenzji", max_length=100)
    rating = models.IntegerField(help_text="ocena użytkownika od 0 do 10") #,validators=[MaxValueValidator(10), MinValueValidator(0)]
    date_created = models.DateField(auto_now_add=True, help_text="Data i czas powstania recenzji")
    date_edited = models.DateField(null=True, help_text="Data i czas ostatniej edycji recenzji")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="Recenzowana książka")

class MediaModel(models.Model):
    image_upload = models.ImageField(upload_to="images/")
    # file_upload = models.FileField(upload_to="files/")