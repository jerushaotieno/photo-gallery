from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here

#  Image Model Tests

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
        test method for deleting image instances after running each test
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
    def test_instances(self):
        '''
        test method for asserting instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_location, Location))
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_image(self):
        '''
        test method for correctly saving an image instance 
        '''
        self.assertTrue(len(Image.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method for correctly deleting an image instance
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method for correctly updating an image instance
        '''
        update_test = self.new_picture.update_image(' ')
        self.assertEqual(update_test.image_link, '')

    def test_get_all(self):
        '''
        test method for retrieving all instances of the image class
        '''
        pictures = Image.get_all()

    def test_get_image_by_id(self):
        '''
        test method for retrieving image instances by id
        '''
        obtained_image = Image.get_image_by_id(self.another_picture.id)

    def test_search_image(self):
        '''
        test method for searching various image instances by category
        '''
        obtained_image = Image.search_image(self.new_picture.category)

    def test_filter_by_location(self):
        '''
        test method for image instances by location
        '''
        obtained_image = Image.filter_by_location(self.another_picture.location)
        print(obtained_image)


#  Location Model Tests

class LocationTest(TestCase):
    '''
    test class for Locations model
    '''
    def setUp(self):
        '''
        test method for creating location instances before any tests are run
        '''
        self.new_location = Location(city='unknown city', country='unknown country')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test method for correctly saving a location instance
        '''
        self.assertTrue(len(Location.objects.all()) == 1)     

    def test_delete_location(self):
        '''
        test method for deleting a location instance correctly 
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_location(self):
        '''
        test method for updating a location instance correctly 
        '''
        update_locale = Location.update_location('unknown location', 'new location')
        self.assertEqual(update_locale.city, 'new location')

    def test_get_all(self):
        '''
        test method for retrieving all instances of the location class 
        '''
        locations = Location.get_all()
        print(locations)


# Categor Model Tests

class CategoryTest(TestCase):
    '''
    test class for categories model
    '''
    def setUp(self):
        '''
        test method for creating category instances before running any tests
        '''
        self.new_category = Category(name='newCategory')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method for deleting category instances after running each test
        '''
        Category.objects.all().delete()

    def test_save_category(self):
        '''
        test method for saving a category instance correctly
        '''
        self.assertTrue(len(Category.objects.all()) == 1)     

    def test_delete_category(self):
        '''
        test method for deleting a category instance correctly
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)    

    def test_update_category(self):
        '''
        test method for updating a category insatnce correctly
        '''
        update_category = Category.update_category('newCategory', 'newCategory2')
        self.assertEqual(update_category.name, 'newCategory2')