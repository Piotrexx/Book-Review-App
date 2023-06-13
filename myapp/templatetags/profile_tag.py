from myapp.models import Review
from django import template

register = template.Library()

@register.inclusion_tag('book_list.html')
def book_list(username):
    reviews = Review.objects.filter(creator__username__icontains=username)
    book_list = [review.book.title for review in reviews]
    return {'books_read':book_list}