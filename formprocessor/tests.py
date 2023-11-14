from django.urls import reverse
from django.test import TestCase, Client
from .models import FormTemplate
import json


class FormProcessorTests(TestCase):
    def setUp(self):
        self.client = Client()
        FormTemplate.objects.create(name="Test Form 1", fields=json.dumps({"email": "email", "phone": "phone"}))
        FormTemplate.objects.create(name="Test Form 2", fields=json.dumps({"date": "date", "text": "text"}))

    def test_matching_form_template(self):
        test_data = {'email': 'test@example.com', 'phone': '+7 123 456 78 90'}
        response = self.client.post(reverse('get_form'), test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('matched_template', response.json())
        self.assertEqual(response.json()['matched_template'], 'Test Form 1')

    def test_no_matching_form_template(self):
        test_data = {'unknown_field': 'some value'}
        response = self.client.post(reverse('get_form'), test_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('matched_template', response.json())
        self.assertEqual(response.json()['unknown_field'], 'text')
