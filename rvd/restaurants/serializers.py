from datetime import date

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Restaurant, Visit


class RestaurantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    average_expense = serializers.SerializerMethodField()
    average_evaluation = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        depth = 1
        fields = (
            "id",
            "user",
            "name",
            "place",
            "type",
            "average_expense",
            "average_evaluation",
            "visit",
        )

    def get_visit_date(self):
        visit_date = self.context["request"].data.get("date")
        if not visit_date:
            return None
        visit_date = visit_date.split("-")
        try:
            year = visit_date[0]
            month = visit_date[1]
            day = visit_date[2]
        except IndexError as e:
            return "Invalid date"

        try:
            return date(year=int(year), month=int(month), day=int(day))
        except ValueError as e:
            return "Invalid date"

    def get_average_evaluation(self, obj):
        visit_date = self.get_visit_date()
        if not visit_date:
            return obj.get_average_evaluation()
        if isinstance(visit_date, str):
            return "Invalid date"
        evaluation = obj.get_average_evaluation(visit_date)
        if not evaluation:
            return "No evaluations for this date"
        return evaluation

    def get_average_expense(self, obj):
        visit_date = self.get_visit_date()
        if not visit_date:
            return obj.get_average_expense()
        if isinstance(visit_date, str):
            return "Invalid date"
        expense = obj.get_average_expense(visit_date)
        if not expense:
            return "No expenses for this date"
        return expense


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("restaurant", "expense", "note", "evaluation")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
        ]
