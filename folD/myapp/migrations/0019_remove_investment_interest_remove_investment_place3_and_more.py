# Generated by Django 4.2.7 on 2024-01-14 07:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0018_investment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="investment",
            name="interest",
        ),
        migrations.RemoveField(
            model_name="investment",
            name="place3",
        ),
        migrations.RemoveField(
            model_name="saving",
            name="place2",
        ),
    ]