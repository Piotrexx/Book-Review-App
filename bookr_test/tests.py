from django.test import TestCase, Client
from .models import Publisher
from django.contrib.auth.models import User
class TestPublisherModel(TestCase):

    def setUp(self):
        self.p = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)
    
    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")

class TestGreetings(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greetings_view(self):
        response = self.client.get('/test/greetings')
        self.assertEquals(response.status_code, 200)

class TestLoggedInGreetingView(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='test@12345password')
        test_user.save()
        self.client = Client()
    
    def test_user_greeting_not_authenticated(self):
        response = self.client.get('/test/greet_user')
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        login = self.client.login(username='testuser', password='test@12345password')
        response = self.client.get('/test/greet_user')
        self.assertEquals(response.status_code, 200)