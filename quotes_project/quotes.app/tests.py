from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Quote

class QuoteModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        author = Author.objects.create(name='Test Author')
        Quote.objects.create(text='Test Quote', author=author, user=user)

    def test_quote_creation(self):
        quote = Quote.objects.get(id=1)
        self.assertEqual(quote.text, 'Test Quote')
        self.assertEqual(quote.author.name, 'Test Author')
