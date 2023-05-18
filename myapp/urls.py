from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books/' ,views.book_list, name="book_list"),
    path('', views.base, name="Home"),
    path('books/<str:id>/', views.detail, name="Detail"),
    path('book_search/', views.book_search, name="book_search"),
    path('publishers/new/',views.publisher_edit, name="publisher_create"),
    path('publishers/<str:pk>/', views.publisher_edit, name="publisher_edit"),
    path('reviews/new/<str:pk>/', views.reviews_post, name="rewiev_post"),

]
