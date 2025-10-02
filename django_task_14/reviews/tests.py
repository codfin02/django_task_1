from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurants.models import Restaurant
from reviews.models import Review


class ReviewAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            nickname='testuser', email='test@example.com', password='password1234'
        )
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant', description='Test Description', address='123 Test St', contact='010-0000-0000'
        )
        self.data = {
            'title': 'Test Review Title',
            'comment': 'Tasty Yammy Yammy~',
        }
        self.client.login(username='test@example.com', password='password1234')

    def test_get_review_list(self):
        Review.objects.create(user=self.user, restaurant=self.restaurant, **self.data)
        url = reverse('review-list', kwargs={'restaurant_id': self.restaurant.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get('title'), self.data['title'])

    def test_post_review(self):
        url = reverse('review-list', kwargs={'restaurant_id': self.restaurant.id})
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('title'), self.data['title'])
        self.assertEqual(Review.objects.count(), 1)

    def test_get_review_detail(self):
        review = Review.objects.create(user=self.user, restaurant=self.restaurant, **self.data)
        url = reverse('review-detail', kwargs={'review_id': review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), review.title)

    def test_update_review(self):
        review = Review.objects.create(user=self.user, restaurant=self.restaurant, **self.data)
        url = reverse('review-detail', kwargs={'review_id': review.id})
        updated = {'title': 'Updated', 'comment': 'Updated body'}
        response = self.client.put(url, updated, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        review.refresh_from_db()
        self.assertEqual(review.title, 'Updated')

    def test_delete_review(self):
        review = Review.objects.create(user=self.user, restaurant=self.restaurant, **self.data)
        url = reverse('review-detail', kwargs={'review_id': review.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)
