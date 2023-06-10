from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="base"),
    path('greet', views.greeting_view, name="greet")
]