from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="nazwa wydawnictwa")

    website = models.URLField(help_text="witryna wydawnictwa")

    email = models.EmailField(help_text="adres email wydawnictwa")

    def __str__(self):
        return self.name
