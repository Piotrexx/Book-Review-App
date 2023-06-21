from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, user_passes_test , login_required
from plotly.offline import plot
import plotly.graph_objs as graphs
from bookr.utils import get_books_read_by_month
@login_required
def profile(request):
    user = request.user
    # print(user)
    permission = user.get_all_permissions()
    # print(permission)
    books_read_by_month = get_books_read_by_month(user.username)

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

    return render(request,'profile.html', {'user':user, 'permission':permission, 'books_read_plot': plot_html})