from email.headerregistry import DateHeader
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http  import Http404, HttpResponse
import datetime as dt

# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to the Photo Gallery')


def photo_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)


def past_days_photo(request,past_date):
        # Converts data from the string Url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(dt.date)
    html = f'''
        <html>
            <body>
                <h1>Photo for {day} {DateTime.day}-{DateHeader.month}-{dt.date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)



