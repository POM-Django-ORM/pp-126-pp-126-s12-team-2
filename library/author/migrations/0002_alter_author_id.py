# Generated by Django 4.1 on 2025-03-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
