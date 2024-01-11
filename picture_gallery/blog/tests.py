from django.test import TestCase
from .models import Blog


class BlogModelTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(
            title='Sample Title',
            category='Sample Category',
            description='Sample Description'
        )

    def test_blog_creation(self):
        """Test the creation of a Blog object"""
        blog = Blog.objects.get(title='Sample Title')
        self.assertEqual(blog.category, 'Sample Category')
        self.assertEqual(blog.description, 'Sample Description')

    def test_blog_str_representation(self):
        """Test the __str__ method of Blog"""
        blog = Blog.objects.get(title='Sample Title')
        self.assertEqual(str(blog), 'Sample Title')
