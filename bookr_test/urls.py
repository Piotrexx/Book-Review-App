from django.urls import path
from .views import *
urlpatterns = [
    path('test/greetings', greeting_view, name="test_greetings"),
    path('test/greet_user', greeting_view_user, name="test_greet_user")
]