from django.test import TestCase
from .models import Todo, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def set_up(self):
        self.daniel = User(username='daniel',email='daniel@gmail.com')
        self.daniel = Profile(user = Self.daniel)