from email.headerregistry import DateHeader
from xmlrpc.client import DateTime
from django.shortcuts import render,redirect
from django.http  import Http404, HttpResponse
import datetime as dt

# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to the Photo Gallery')


def photos_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})


# View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})



