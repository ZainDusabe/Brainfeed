# Generated by Django 4.1.3 on 2022-11-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainfeeds', '0002_alter_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default='Customer', max_length=200),
        ),
    ]