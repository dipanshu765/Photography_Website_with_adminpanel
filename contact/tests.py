from django.test import TestCase
from .models import Contact
from django.utils import timezone


class ContactModelTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            message='Test message for testing purposes'
        )

    def test_contact_creation(self):
        """Test the creation of a Contact object"""
        contact = Contact.objects.get(name='John Doe')
        self.assertEqual(contact.email, 'johndoe@example.com')
        self.assertEqual(contact.message, 'Test message for testing purposes')
        self.assertTrue(contact.date <= timezone.now())  # Check date is within a reasonable range

    def test_contact_str_representation(self):
        """Test the __str__ method of Contact"""
        contact = Contact.objects.get(name='John Doe')
        self.assertEqual(str(contact), 'John Doe-johndoe@example.com')
