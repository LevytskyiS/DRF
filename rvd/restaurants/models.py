from decimal import getcontext, Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_all_visits(self):
        return self.visit.all()

    def get_average_expense(self, *args):
        getcontext().prec = 3

        if not args:
            expenses = [Decimal(str(visit.expense)) for visit in self.get_all_visits()]
        else:
            expenses = [
                Decimal(str(visit.expense)) for visit in self.visit.filter(date=args[0])
            ]

        if not expenses:
            return 0

        return Decimal(str(sum(expenses))) / Decimal(str(len(expenses)))

    def get_average_evaluation(self, *args):
        getcontext().prec = 3

        if not args:
            ratings = [
                Decimal(str(visit.evaluation)) for visit in self.get_all_visits()
            ]
        else:
            ratings = [
                Decimal(str(visit.evaluation))
                for visit in self.visit.filter(date=args[0])
            ]

        if not ratings:
            return 0

        return Decimal(str(sum(ratings))) / Decimal(str(len(ratings)))


class Visit(models.Model):
    EVALUATION_CHOICES = {
        1: "Awful",
        2: "Bad",
        3: "OK",
        4: "Good",
        5: "Perfect",
    }
    restaurant = models.ForeignKey(
        Restaurant, related_name="visit", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    expense = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0, "The expense must be equal or greater than 0.")
        ],
    )
    note = models.TextField(max_length=1000)
    evaluation = models.IntegerField(choices=EVALUATION_CHOICES)

    def __str__(self):
        return f"{self.restaurant.user.username} - {self.restaurant.name} visit"
