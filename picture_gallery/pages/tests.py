from django.test import TestCase
from .models import Content, Gallery, Team


class ContentModelTestCase(TestCase):
    def setUp(self):
        Content.objects.create(
            title='Sample Title',
            category='Sample Category',
            description='Sample Description'
        )

    def test_content_creation(self):
        """Test the creation of a Content object"""
        content = Content.objects.get(title='Sample Title')
        self.assertEqual(content.category, 'Sample Category')
        self.assertEqual(content.description, 'Sample Description')

    def test_content_str_representation(self):
        """Test the __str__ method of Content"""
        content = Content.objects.get(title='Sample Title')
        self.assertEqual(str(content), 'Sample Title')

class GalleryModelTestCase(TestCase):
    def setUp(self):
        Gallery.objects.create(
            name='Sample Name',
            category='Sample Category'
        )

    def test_gallery_creation(self):
        """Test the creation of a Gallery object"""
        gallery = Gallery.objects.get(name='Sample Name')
        self.assertEqual(gallery.category, 'Sample Category')

    def test_gallery_str_representation(self):
        """Test the __str__ method of Gallery"""
        gallery = Gallery.objects.get(name='Sample Name')
        self.assertEqual(str(gallery), 'Sample Name - Sample Category')

class TeamModelTestCase(TestCase):
    def setUp(self):
        Team.objects.create(
            member_name='Sample Member',
            post='Sample Post'
        )

    def test_team_creation(self):
        """Test the creation of a Team object"""
        team = Team.objects.get(member_name='Sample Member')
        self.assertEqual(team.post, 'Sample Post')

    def test_team_str_representation(self):
        """Test the __str__ method of Team"""
        team = Team.objects.get(member_name='Sample Member')
        self.assertEqual(str(team), 'Sample Member - Sample Post')
