# Generated by Django 4.1.3 on 2022-11-24 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brainfeeds', '0009_alter_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
