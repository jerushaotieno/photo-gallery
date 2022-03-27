from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here

class ImageTest(TestCase):
    '''
    testing image model
    '''
    def setUp(self):
        '''
        Creates image instances called before any tests are run 
        '''
        self.new_category = Category(name='testing')
        self.new_category.save_category()
        
        self.new_location = Location(city='Nairobi', country='Kenya')
        self.new_location.save_location()
        
        self.new_picture = Image(image_link=' ', title=' ', description=' ', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Image(image_link='', title=' ', description=' ', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Image.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('images/updated.png')
        self.assertEqual(update_test.image_link, 'images/updated.png')

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = Image.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Image.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Image.search_image(self.new_picture.category)
        # print(obtained_image) #todo: reference individual instances

    def test_filter_by_location(self):
        '''
        test method to obtain image insatnces by location
        '''
        obtained_image = Image.filter_by_location(self.another_picture.location)
        print(obtained_image)
