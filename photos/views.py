from email.headerregistry import DateHeader
from xmlrpc.client import DateTime
from django.shortcuts import render,redirect
from django.http  import Http404, HttpResponse
import datetime as dt

from photos.models import Image, Location

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


# Photo Gallery

def gallery(request):
    picture = Image.get_all()
    location = Location.get_all()
    return render(request, 'gallery.html', {'picture': picture, 'location':location})



# Search by category

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_for = request.GET.get('category')
        result = Image.search_image(search_for)
        message = f'{search_for}'

        return render(request, 'search.html', {'message':message, 'result':result})
    else:
        message = 'Type something else to search for'
        return render(request, 'search.html', {'message':message}) 


# Location 

def location(request,locale):
    image = Image.filter_by_location(locale)
    return render(request, 'location.html', {'results':image})