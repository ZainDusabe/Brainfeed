# Generated by Django 4.1.3 on 2022-11-17 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brainfeeds', '0007_remove_author_institute_remove_author_password1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='Username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
