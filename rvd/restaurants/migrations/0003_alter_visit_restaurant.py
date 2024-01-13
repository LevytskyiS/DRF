# Generated by Django 5.0.1 on 2024-01-13 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_visit_evaluation_alter_visit_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit', to='restaurants.restaurant'),
        ),
    ]