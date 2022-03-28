from email.headerregistry import DateHeader
from xmlrpc.client import DateTime
from django.shortcuts import render,redirect
from django.http  import Http404, HttpResponse
import datetime as dt

from photos.models import Image

# Create your views here.

def homepage(request):
    return render (request,'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})


# View Function to present photos from past days
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



# Search by category

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'results':res})
    else:
        message = 'Type in what to search for'
        return render(request, 'search.html', {'message':message}) 