# My Django Book Review Website

## Introduction

In this project I learn basics of Django framework for Python programming language.
Website is about posting rewievs of books, adding books and more. 
I learn Django from this book [Web Development with Django](https://www.amazon.com/Web-Development-Django-applications-Python-based/dp/1839212500)
I really recommend this book for beginners, it's really well documented.

## Contributing

I welcome anyone who want to contribute in this project !
- If you noticed any bugs in my application you can let me know about it, don't be shy !


### Requirements for running this on your PC 

- [Python](https://www.python.org/downloads/)

### Installing Django framework 

```shell
python pip install Django
```

### Installing Djnago rest API framework (DRF)

```shell
pip install djangorestframework
```

### Installing crispy-forms

```shell
pip install django-crispy-forms
```

```shell
pip install crispy_bootstrap4 
```

### Running develpment server

```shell
python manage.py runserver
```
### Cloning the repository

```shell
git clone https://github.com/Piotrexx/Django_books_project.git
```

### Changing password
```shell
python manage.py changepassword username
```

### Starting test
```shell
python manage.py test
```
<!-- # WARNING !

**IT IS WORTH TO NOTICE THAT I DON'T PUT ALL THE FILES IN THE REPOSITORY !**

I don't put files like: 
 - files from folder __pychache__
 - files from folder __migrations__


Those files goes with the Django framework when app or project created.

For better experiance first create project like this:

```shell
django-admin startproject project_name
```

And then create an app just like this:

```shell
python manage.py startapp app_name
```

When everything is readym you can copy files from the repository.

**Files from bookr folder goes to your project folder**

**Files from myapp folder goes to your app folder** -->




*This project is not focused on looks so don't blame me.*