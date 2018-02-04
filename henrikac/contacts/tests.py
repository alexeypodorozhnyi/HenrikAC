from django.test import TestCase
from django.urls import reverse

from . import forms


class ContactViewTest(TestCase):
    """Testing contact view, url and template"""
    def test_contact_get_request(self):
        """Testing contact get request"""
        resp = self.client.get(reverse('contact:contact_me'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Want to get in touch with me?')
        self.assertTemplateUsed(resp, 'contacts/contact.html')

    def test_contact_post_request(self):
        """Testing contact post request"""
        resp = self.client.post(reverse('contact:contact_me'))
        self.assertEqual(resp.status_code, 200)

    def test_valid_contact_form(self):
        """Testing a valid form"""
        form_data = {'name': 'Henrik Christensen', 'email': 'test@email.com', 'message': 'Test message'}
        form = forms.ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form_no_name(self):
        """Testing an invalid form with an empty name field"""
        form_data = {'name': '', 'email': 'test@email.com', 'message': 'Test message'}
        form = forms.ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_contact_form_no_email(self):
        """Testing an invalid form with an empty email field"""
        form_data = {'name': 'Henrik Christensen', 'email': '', 'message': 'Test message'}
        form = forms.ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_contact_form_no_message(self):
        """Testing an invalid form with an empty message field"""
        form_data = {'name': 'Henrik Christensen', 'email': 'test@email.com', 'message': ''}
        form = forms.ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
