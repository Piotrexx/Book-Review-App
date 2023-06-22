import datetime

from django.db.models import Count
from myapp.models import Review

def get_books_read_by_month(username):
    current_year = datetime.datetime.now().year
    books = Review.objects.filter(creator__username__contains=username, date_created__year=current_year).values('date_created__month').annotate(book_count=Count('book__title'))
    print(Review.objects.filter(creator__username__contains=username, date_created__year=current_year).values('date_created__month'))

    return books

import xlsxwriter

def create_workbook(filename):
    workbook = xlsxwriter.Workbook(filename)
    return workbook

def create_worksheet(workbook):
    worksheet = workbook.add_worksheet()
    return worksheet

def write_data(worksheet, data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row,col,data[row][col])

def close_workbook(workbook):
    workbook.close()
