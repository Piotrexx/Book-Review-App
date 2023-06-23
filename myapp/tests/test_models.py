from myapp.models import Publisher
from django.test import TestCase

class TestingModels(TestCase):

    def setUp(self):
        self.p = Publisher(name = "Pocket Books", website = "https://pocketbookssampleurl.com", email = "pocketbook@example.com")
    

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)