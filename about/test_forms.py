from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """test for the name field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(), msg = 'Names was not provided, but test is valid!'
        )
    def test_email_is_required(self):
        """test for email field"""
        form = CollaborateForm({
            'name': 'Joeski',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(), msg = 'Email not provided but test is valid!'
        )

    def test_message_is_required(self):
        """test for message field"""
        form = CollaborateForm({
            'name': 'Joeski',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(), msg = 'Message is not rpovided but test isvalid'
        )