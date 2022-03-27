from email.mime import image
from django.db import models

# Create your models here.

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
        searched_image = cls.objects.filter(category__name__contains=cat)
        return searched_image

    @classmethod
    def filter_by_location(cls ,location):
        '''
        method filters images by locations
        '''
        filtered_image = Image.objects.filter(location__city__contains=location)
        return filtered_image