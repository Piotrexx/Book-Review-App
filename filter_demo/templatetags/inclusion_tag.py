from django import template

register = template.Library()

@register.inclusion_tag('test.html')
def test(books):
    test = [book_name for book_name, book_author in books.items()]
    return {'test':test}