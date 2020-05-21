from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import post

from django.urls import reverse

# Create your tests here.

class blogtest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = post.objects.create(
            Title='A good title',
            Body='Nice body content',
            Author=self.user,
        )

    def test_title(self):
        self.assertEqual(f'{self.post.Author}','testuser')

    def test_post_content(self):
        self.assertEqual(f'{self.post.Title}', 'A good title')

        self.assertEqual(f'{self.post.Author}', 'testuser')
        self.assertEqual(f'{self.post.Body}', 'Nice body content')

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'A good title')


