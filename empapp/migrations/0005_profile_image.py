# Generated by Django 5.0.3 on 2024-05-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
