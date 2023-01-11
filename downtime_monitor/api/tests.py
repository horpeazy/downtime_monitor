from django.test import TestCase

# Create your tests here.

class SimpleTest(TestCase):
    def test_adding_two_numbers(self):
        x = 1 + 1
        self.assertEqual(x, 2)
