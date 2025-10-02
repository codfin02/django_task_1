from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurants.models import Restaurant


class RestaurantModelTest(APITestCase):
    def setUp(self):
        self.restaurant_info = {
            "name": "Test Restaurant",
            "description": "Test Description",
            "address": "Test Address",
            "contact": "Test Contact",
            "open_time": "10:00:00",
            "close_time": "22:00:00",
            "last_order": "21:00:00",
            "regular_holiday": "MON",
        }

    def test_create_restaurant_model(self):
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(str(restaurant), self.restaurant_info['name'])


class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        self.restaurant_info = {
            "name": "Test Restaurant",
            "description": "Test Description",
            "address": "Test Address",
            "contact": "Test Contact",
            "open_time": "10:00:00",
            "close_time": "22:00:00",
            "last_order": "21:00:00",
            "regular_holiday": "MON",
        }
        user = get_user_model().objects.create_user(email='test@example.com', password='password1234')
        self.client.login(username='test@example.com', password='password1234')

    def test_restaurant_list_view(self):
        url = reverse('restaurant-list')
        Restaurant.objects.create(**self.restaurant_info)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results', response.data)), 1)

    def test_restaurant_post_view(self):
        url = reverse('restaurant-list')
        response = self.client.post(url, self.restaurant_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)

    def test_restaurant_detail_view(self):
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), self.restaurant_info['name'])

    def test_restaurant_update_view(self):
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})
        updated = {
            "name": "Updated Restaurant",
            "description": "Updated Description",
            "address": "Updated Address",
            "contact": "Updated Contact",
            "open_time": "11:00:00",
            "close_time": "23:00:00",
            "last_order": "22:00:00",
            "regular_holiday": "TUE",
        }
        response = self.client.put(url, updated, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(response.data.get('name'), updated['name'])

    def test_restaurant_delete_view(self):
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)

