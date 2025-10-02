from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.signup_data = {
            'nickname': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword1234',
        }

    def test_user_signup(self):
        resp = self.client.post(reverse('user-signup'), self.signup_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(resp.data.get('nickname'), 'testuser')
        self.assertEqual(resp.data.get('email'), 'test@example.com')

    def test_user_login(self):
        User.objects.create_user(**self.signup_data)
        data = {'email': self.signup_data['email'], 'password': self.signup_data['password']}
        resp = self.client.post(reverse('user-login'), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('message'), 'login successful.')

    def test_user_login_invalid_credentials(self):
        data = {'email': 'test@example.com', 'password': 'wrong'}
        resp = self.client.post(reverse('user-login'), data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_details(self):
        user = User.objects.create_user(**self.signup_data)
        self.client.login(username=self.signup_data['email'], password=self.signup_data['password'])
        resp = self.client.get(reverse('user-detail', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('nickname'), 'testuser')
        self.assertEqual(resp.data.get('email'), 'test@example.com')

    def test_update_user_details(self):
        user = User.objects.create_user(**self.signup_data)
        self.client.login(username=self.signup_data['email'], password=self.signup_data['password'])
        data = {'nickname': 'updated', 'password': 'newpass1234'}
        resp = self.client.patch(reverse('user-detail', kwargs={'pk': user.id}), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('nickname'), 'updated')
        user.refresh_from_db()
        self.assertTrue(check_password('newpass1234', user.password))

    def test_delete_user(self):
        user = User.objects.create_user(**self.signup_data)
        self.client.login(username=self.signup_data['email'], password=self.signup_data['password'])
        resp = self.client.delete(reverse('user-detail', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(email=self.signup_data['email']).exists())
