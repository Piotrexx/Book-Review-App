from django.urls import path, include
from . import views, api_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('books/' ,views.book_list, name="book_list"),
    path('', views.base, name="Home"),
    path('books/<int:id>/', views.detail, name="Detail"),
    path('book_search/<str:value>/', views.base, name="book_search"),
    path('publishers/new/',views.publisher_edit, name="publisher_create"),
    path('publishers/<str:pk>/', views.publisher_edit, name="publisher_edit"),
    # path('books/<int:book_pk>/reviews/<int:reviewer_pk>/', views.reviews_post, name='reviews_edit'),
    # path('books/<int:book_pk>/review/new', views.reviews_post, name='review_create')
    path('books/<int:book_pk>/reviews/new/',views.reviews_post, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.reviews_post, name='review_edit'),
    path('books/<int:pk>/media_form/', views.media_form, name="media_form"),
    path('api/login', api_views.Login.as_view(), name="login")

    # APIs

    # path('api/all_books/', api_views.AllBooks.as_view() , name="all_books"),
    # path('api/contribs', api_views.BookAndContributors.as_view(), name="contribs"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
