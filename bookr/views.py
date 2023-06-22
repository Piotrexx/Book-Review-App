from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, user_passes_test , login_required
from plotly.offline import plot
import plotly.graph_objs as graphs
from bookr.utils import *
from myapp.models import Review, Book
from django.db.models import Count
from django.http import HttpResponse
@login_required
def profile(request):
    user = request.user
    # print(user)
    permission = user.get_all_permissions()
    # print(permission)
    books_read_by_month = get_books_read_by_month(user.username)

#     print(Review.objects.filter(creator__username__contains=user.username))
      
#     print(Review.objects.filter(creator__username__contains=user.username).values('date_created__month').annotate(book_count=Count('book__title')))
    months = [i+1 for i in range(12)]
    books_read = [0 for _ in range(12)]

    for num_books_read in books_read_by_month:
            list_index = num_books_read['date_created__month'] - 1
            books_read[list_index] = num_books_read['book_count']
        
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=months, y=books_read)
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Month",yaxis_title="Number of books read")
    plot_html = plot(figure, output_type='div')
    # print(books_read)




    return render(request,'profile.html', {'user':user, 'permission':permission, 'books_read_plot': plot_html})


def books_read(request):
    user = request.user
    books = []
    data = []
    books_read = Review.objects.filter(creator_id=user)
    for i in books_read:
        books += Book.objects.filter(id=i.book_id)


    for item in books:
        data.append([item.title, item.publication_date, item.isbn])
     
    workbook = create_workbook('books_read.xlsx')
    worksheet = create_worksheet(workbook)
    write_data(worksheet, data)
    close_workbook(workbook)

    return HttpResponse("heelo")
