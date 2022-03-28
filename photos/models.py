from email.mime import image
from django.db import models

# Create your models here.

# Image Model

class Image(models.Model):
    '''
    for images
    '''
    image_link = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, default=1)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def save_image(self):
        '''
        method saves image
        '''
        self.save()

    def delete_image(self):
        '''
        method deletes image
        '''
        self.delete()

    def update_image(self, new_url):
        '''
        method updates image link
        '''
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('This image does not exist')

    @classmethod
    def get_all(cls):
        '''
        method retrieves all images
        '''
        photos = image.objects.all()
        return photos

    @classmethod
    def get_image_by_id(cls, id):
        '''
        method retrieves images by unique id
        '''
        retrieved_image = Image.objects.get(id = id)
        return retrieved_image

    @classmethod
    def search_image(cls, cat):
        '''
        method searches all images by category
        '''
        searched_image = cls.objects.filter(category__name__icontains=cat)
        return searched_image

    @classmethod
    def filter_by_location(cls ,location):
        '''
        method filters images by locations
        '''
        filtered_image = Image.objects.filter(location__city__contains=location)
        return filtered_image


# Location Model

class Location(models.Model):
    '''
    model handles location factor
    '''
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        '''
        method saves a location
        '''
        self.save()

    def delete_location(self):
        '''
        method deletes a location
        '''
        self.delete()

    @classmethod
    def update_location(cls, search_term , new_locale):
        '''
        method updates a location's city name
        '''
        try:
            to_update = Location.objects.get(country = search_term)
            to_update.city = new_locale
            to_update.save()
            return to_update
        except Location.DoesNotExist:
            print('That location does not exist')

    @classmethod
    def get_all(cls):
        '''
        method retrieves all stored locations
        '''
        cities = Location.objects.all()
        return cities


# Category Model

class Category(models.Model):
    '''
    model handles category options
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        method saves a category
        '''
        self.save()

    def delete_category(self):
        '''
        method deletes a category
        '''
        self.delete()

    @classmethod
    def update_category(cls, search_term , new_cat):
        '''
        method updates chosen category
        '''
        try:
            to_update = Category.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Category.DoesNotExist:
            print('This category does not exist')