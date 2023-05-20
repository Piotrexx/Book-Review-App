from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books/' ,views.book_list, name="book_list"),
    path('', views.base, name="Home"),
    path('books/<int:id>/', views.detail, name="Detail"),
    path('book_search/', views.book_search, name="book_search"),
    path('publishers/new/',views.publisher_edit, name="publisher_create"),
    path('publishers/<str:pk>/', views.publisher_edit, name="publisher_edit"),
    # path('books/<int:book_pk>/reviews/<int:reviewer_pk>/', views.reviews_post, name='reviews_edit'),
    # path('books/<int:book_pk>/review/new', views.reviews_post, name='review_create')
    path('books/<int:book_pk>/reviews/new/',views.reviews_post, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.reviews_post, name='review_edit'),
]
