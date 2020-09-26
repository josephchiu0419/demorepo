from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def setup(self):
        Post.objects.create(title="Test title 1",content="Thsi is content test1", author="josephchiu")
        Post.objects.create(title="Test title 2", content="This is content test2", author="josephchiu")

# Create your tests here.
