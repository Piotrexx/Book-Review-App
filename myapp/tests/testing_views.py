from bookr.views import profile
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser


class TestingViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username="TestUser", password="TestUser123@")
        self.test_user.save()
        self.factory = RequestFactory()

    def TestIfUserIsNotAuth(self):
        request = self.factory.get('/accounts/profile')
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEquals(response.status_code, 302)
    
    def TestIfUserAuth(self):
        request = self.factory.get('/accounts/profile')
        request.user = self.test_user
        response = profile(request)
        self.assertEquals(response.status_code, 200)
