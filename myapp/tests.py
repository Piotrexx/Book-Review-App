from django.test import TestCase

# Create your tests here.

class TestSimpleComponent(TestCase):
    def test_basic_sum(self):
        assert 1+1 == 2