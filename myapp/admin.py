from django.contrib import admin
from myapp.models import Publisher, Contributor, Book, BookContributor, Review
from django.contrib.admin import ModelAdmin
# Register your models here.

# funkcja która z imienia robi inicjały
def initials(item):
    initials = ''.join([name[0] for name in item.first_names.split(' ')])
    return "{}, {}".format(item.last_names, initials)

# konfiguracja panelu Book
class BookAdmin(ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title','isbn','publisher')
    list_filter = ('publisher',)
    search_fields = ('title', 'isbn', 'publisher__name')

# konfiguracja panelu Review
class ReviewAdmin(ModelAdmin):
    exclude = ('date_edited',)
    # fields = ('content', 'rating','creator', 'book')
    fieldsets = (('Łącza', {'fields':('creator', 'book')}), ('Zawartość recenzji', {'fields':('content','rating')}))
    
# konfiguracja panelu Contributor
class ContributorAdmin(ModelAdmin):
    list_display = (initials,)
    list_filter = ('first_names', 'last_names')


# rejestr tabel sql by pokazały się w panelu administracyjnym
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
