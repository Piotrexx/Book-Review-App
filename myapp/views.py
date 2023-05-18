from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Review, BookContributor, Contributor, Publisher
from .utils import average_rating
from django.shortcuts import get_object_or_404, redirect
from .forms import *
from django.contrib import messages
from django.utils import timezone

def reviews_post(request, pk, reviewer_id=None):
    pk = get_object_or_404(Book, title=pk)

    if reviewer_id is not None:
        reviewer = get_object_or_404(Review, book_id=pk, pk=reviewer_id)

    else:
        reviewer = None

        print(reviewer)
        print(reviewer_id)
        print(pk)
    
    books = Book.objects.all()
    # print(pk)

    for book in books:
        if book == pk:
            break
        else:
            continue

    if request.method == "POST":
        form = ReviewsForm(request.POST, instance=reviewer)
        if form.is_valid():
            created_review = form.save(False)
            created_review.book = book
            if reviewer is None:
                pass
            else:
                created_review.date_edited = timezone.now()

                created_review.save()
            messages.success(request, "Recenzja została dodana")
            # print(book)
            return redirect(f"/books/{book.title}", book.pk)








    form = ReviewsForm(instance=reviewer)
    return render(request, 'review_form.html', {'form':form, 'book':book, 'pk':pk})



def publisher_edit(request, pk=None):
    print(pk)
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



def base(request, value=None):
    jaja = "jaja byka"
    error = ""
    search_list = ""
    main_form = SeachForm()
    if request.method == "GET":
        main_form = SeachForm(request.GET)
        if main_form.is_valid():

            for name, value in main_form.cleaned_data.items():
                search_list = Book.objects.filter(title__icontains=value) | Contributor.objects.filter(first_names__icontains=value) | Contributor.objects.filter(last_names__icontains=value)
            if value == None:
                error = "nic nie znaleziono"
    else:
        main_form = SeachForm()
        value = ""
       
    

        

    return render(request,'base.html', {"main_form": main_form,"jaja":jaja, "error": error, "search_list": search_list, 'value': value,} )

def book_search(request, value=None):
    error = ""
    search_list = ""
    if request.method == "GET":
        form = MoreForms(request.GET)
        if form.is_valid():

            for name, value in form.cleaned_data.items():
                search_list = Book.objects.filter(title__icontains=value)

                
    else:
        form = MoreForms()
        
        

    return render(request, 'book_search.html', {"form": form, "error": error, "search_list": search_list, 'value': value, })

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
        print(book)
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
    id = get_object_or_404(Book, title=id) # jeżeli takie id istnieje to wtedy wzraca wartość (id=id) albo wywala 404
    # print(id)
    reviews = Review.objects.all() # pobiera wszystkie recenzje
    info_list = []
    books = Book.objects.all()
    
    for book in books:
        print(book)
        if book == id:
            break
        else:
            continue
    

    if reviews: # jeżeli cokolwiek jest w recenzjach
        no = ""
        for i in reviews: # pętla która zapętla się po arrayu recenzji 
            
            id_of_review = Review.objects.get(book_id=i) # id recenzji książki to liczba i (czyli liczba powtórzeń) 
            
            if id_of_review == id: # jeżeli id recenzji książki równa się id książki 
                content = Review.objects.get(content=i)
                book_rating = average_rating([review.rating for review in reviews])
                # to się jeszcze dokończy :P
            else:
                print("Bye")
    else: 
        book_rating = "No reviews !"
        no = "There is no reviews yet !"
        content = ""
    return render(request, 'details.html', {'no': no, 'book':book, 'content': content, 'book_rating': book_rating})


