from django.test import TestCase
from django.contrib.auth.models import User


from ..models import Restaurant


class RestaurantTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="user", email="qwe@gmail.com", password="qwe2Werrr"
        )
        Restaurant.objects.create(user=user, name="MAC", place="NY", type="German")

    def test_restaurant_attributes(self):
        obj = Restaurant.objects.get(name="MAC")
        self.assertEqual("MAC", obj.name)
        self.assertEqual("NY", obj.place)
        self.assertEqual("German", obj.type)
