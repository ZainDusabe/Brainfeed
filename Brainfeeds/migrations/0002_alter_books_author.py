# Generated by Django 4.1.3 on 2022-11-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brainfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Brainfeeds.author'),
        ),
    ]