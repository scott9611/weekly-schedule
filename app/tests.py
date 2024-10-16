from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from app.database.models import TimeSlot, WeeklySchedule

class WeeklyScheduleTests(APITestCase):

    def setUp(self):
        """
        Set up the test environment before each test method is run.
        This method initializes the API client, creates a test user,
        and sets up the admin client for authenticated requests.
        """
        self.client = APIClient()
        self.url = reverse('weeklyschedule-list')

        self.user = User.objects.create_user(username='admin', password='12345')
        self.user.is_active = True
        self.user.save()

        self.admin_client = APIClient()
        self.admin_client.login(username='admin', password='12345')

    def obtain_token(self):
        """
        Obtain an authentication token for the test user.
        This method sends a POST request to the token endpoint and
        sets the obtained token as the authorization header for subsequent requests.
        """
        response = self.client.post('/api/token/', data={"username": "admin", "password": "12345"}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_create_weekly_schedule(self):
        """
        Test the creation of a weekly schedule.
        This method sends a POST request to create a new weekly schedule
        and asserts that the response status code is 201 (Created).
        """
        self.obtain_token()
        data = {
            "monday": [
                {"start": "08:00", "stop": "12:00", "ids": [1, 2]}
            ],
            "tuesday": [
                {"start": "10:00", "stop": "14:00", "ids": [3, 4]}
            ],
            "wednesday": [
                {"start": "09:00", "stop": "11:00", "ids": [5, 6]}
            ],
            "thursday": [
                {"start": "11:00", "stop": "13:00", "ids": [7, 8]},
                {"start": "14:00", "stop": "16:00", "ids": [9, 10]}
            ],
            "friday": [
                {"start": "08:00", "stop": "10:00", "ids": [11, 12]}
            ],
            "saturday": [
                {"start": "12:00", "stop": "14:00", "ids": [13, 14]}
            ],
            "sunday": [
                {"start": "09:00", "stop": "11:00", "ids": [15, 16]}
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_weekly_schedules(self):
        """
        Test retrieving all weekly schedules.
        This method sends a GET request to fetch all weekly schedules
        and asserts that the response status code is 200 (OK).
        """
        self.obtain_token()
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_weekly_schedule(self):
        """
        Test updating a weekly schedule.
        This method sends a PUT request to update an existing weekly schedule
        and asserts that the response status code is 200 (OK).
        """
        self.obtain_token()
        schedule = WeeklySchedule.objects.create()
        url = reverse('weeklyschedule-detail', args=[schedule.pk])
        data = {
            "monday": [
                {"start": "08:30", "stop": "12:30", "ids": [1, 3]}
            ],
            "tuesday": [
                {"start": "10:30", "stop": "14:30", "ids": [4, 5]}
            ],
            "wednesday": [
                {"start": "09:30", "stop": "11:30", "ids": [6, 7]}
            ],
            "thursday": [
                {"start": "11:30", "stop": "13:30", "ids": [8, 9]},
                {"start": "14:30", "stop": "16:30", "ids": [10, 11]}
            ],
            "friday": [
                {"start": "08:30", "stop": "10:30", "ids": [12, 13]}
            ],
            "saturday": [
                {"start": "12:30", "stop": "14:30", "ids": [14, 15]}
            ],
            "sunday": [
                {"start": "09:30", "stop": "11:30", "ids": [16, 17]}
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_weekly_schedule(self):
        """
        Test deleting a weekly schedule.
        This method sends a DELETE request to remove an existing weekly schedule
        and asserts that the response status code is 204 (No Content).
        """
        self.obtain_token()
        schedule = WeeklySchedule.objects.create()
        url = reverse('weeklyschedule-detail', args=[schedule.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
