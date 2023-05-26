from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from django.shortcuts import get_object_or_404, redirect
from .forms import *
from django.contrib import messages
from django.utils import timezone

def reviews_post(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewsForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, "Review for \"{}\" created.".format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Review for \"{}\" updated.".format(book))

            updated_review.save()
            return redirect("Detail", book.pk)
    else:
        form = ReviewsForm(instance=review)

    return render(request, "review_form.html",
                  {"form": form,
                   "instance": review,
                   "model_type": "Review",
                   "related_instance": book,
                   "related_model_type": "Book"
                   })
def publisher_edit(request, pk=None):
    # print(pk)
    if pk is not None:
        publisher = get_object_or_404(Publisher, name=pk)   
    else:
        publisher = None
    
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Obiekt Publisher \"{}\" został utworzony.".format(updated_publisher))
                

                
            else:
                messages.success(request, "Obiekt Publisher \"{}\" został uaktualniony.".format(updated_publisher))
                return redirect("publisher_edit", updated_publisher.name)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'form-example.html', {"method": request.method, "form": form})





def media_form(request, pk):
    instance = None
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save()
            return redirect('Detail', book.pk) 
    else:
        form = UploadForm()

    return render(request, "media_form.html", {"form": form, "instance": instance})

def base(request, value=None):
    error = ""
    search_list = ""
    if request.method == "GET":
        main_form = SeachForm(request.GET)
        if main_form.is_valid():

            for name, value in main_form.cleaned_data.items():
                search_list = Book.objects.filter(title__icontains=value)
                #| Contributor.objects.filter(first_names__icontains=value) | Contributor.objects.filter(last_names__icontains=value)
            if search_list == None:
                error = "nic nie znaleziono"
            
                return redirect('book_search', value)
    else:
        main_form = SeachForm()
        value = ""
        
       
  

        

    return render(request,'base.html', {"main_form": main_form, "error": error, "search_list": search_list, 'value': value,} )

def book_list(request):

    books = Book.objects.all() # pobiera dane z bazy danych na temat wszystkich książek
    book_list = [] # tworzenie listy książek
    i = 0
    for book in books:
        i+=1
        reviews = book.review_set.all() # pobieramy informacje o recenzjach (trzeba dodać review_set bo jest Foreignkey)
        # test = 0
        # test += 1
        # print(reviews)
        if reviews: # jeżeli reviews istnienją (są prawdą)
            book_rating = average_rating([review.rating for review in reviews]) # obliczamy średnią ocene książki, kożystamy z funkcji average_rating którą stworzyliśmy w pliku utils 
            number_of_reviews = len(reviews) # liczba wszyskich recenzji to liczba długości arraya reviews
            
        else: 
            book_rating = None # nie ma żadnych recenzji 
            number_of_reviews = 0 # liczba recenzji to zero
        # print(book)
        # id_test = Review.objects.get(book_id=book)
        # print(id_test)
        book_list.append({ # dodanie wszystkich informacji do objectu który przechowuje zmienne HTML-owe
            'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews,
            'i':i
        })
        context = {'book_list': book_list}
    return render(request, 'book_list.html', context)


def detail(request, id):
    id = get_object_or_404(Book, id=id) # jeżeli takie id istnieje to wtedy wzraca wartość (id=id) albo wywala 404
    # print(id)
    reviews = Review.objects.all() # pobiera wszystkie recenzje
    rev_list = []
    books = Book.objects.all()

    for book in books:
        # print(book)
        if book == id:
            break
        else:
            continue
    
   
    # instance = MediaModel.objects.filter(image_upload="images/"+book.title.replace(" ","_")+".png")
   
    instance = MediaModel.objects.get(image_upload="images/Advanced_Deep_Learning_with_Keras.png")
    url = instance.image_upload.url
    # print("images/"+book.title.replace(" ","_")+".png")
    if reviews: # jeżeli cokolwiek jest w recenzjach
        no = ""
        number_of_reviews = len(reviews)
        book_rating = average_rating([review.rating for review in reviews])
        # print(book_rating)
        for review in reviews: # pętla która zapętla się po arrayu recenzji 
            # print(review)
            # print(review.pk)
            id_of_review = Review.objects.filter(book_id=id) # id recenzji książki to liczba i (czyli liczba powtórzeń) 
            # print(id_of_review)
            if id_of_review == id: # jeżeli id recenzji książki równa się id książki 
                content = Review.objects.get(content=review)
                
            else:
                content =""
            rev_list.append({
                'review': review,
                'number_of_reviews': number_of_reviews,
                "content":content
            })
    else: 
        book_rating = None
        no = "There is no reviews yet !"
        content = ""
        review = None

    
    return render(request, 'details.html', {"url":url,'no': no, 'book':book, 'content': content, 'book_rating': book_rating, "review": review, 'rev_list':rev_list})


