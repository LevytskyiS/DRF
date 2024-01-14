from django.urls import reverse
from rest_framework.test import APITestCase


class RestaurantAPITestCase(APITestCase):
    def test_get(self):
        url = reverse("restaurant-list")
        response = self.client.get(
            url,
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1MjM5NDY0LCJpYXQiOjE3MDUxODc1ODIsImp0aSI6IjQyMjRmOTYwOWFkZTRiYjY5ODQyNWRjYTg5MzdhNTliIiwidXNlcl9pZCI6MX0.4phEPEeNc2gs5lSvsAkDPwt290NffR2N1Ve69NubTbI"
            },
        )
        # No registered user at the moment
        self.assertNotEqual(200, response.status_code)
        self.assertEqual(401, response.status_code)
