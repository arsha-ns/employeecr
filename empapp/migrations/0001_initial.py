# Generated by Django 5.0.3 on 2024-03-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
