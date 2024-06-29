from django.db import models

# Create your models here.
class Employee(models.Model):

    name=models.CharField(max_length=100)

    department=models.CharField(max_length=100)

    salary=models.CharField(max_length=100)

    location=models.CharField(max_length=100)
    
    address=models.CharField(max_length=100)


    def __str__(self):

        return self.name


class profile(models.Model):

    name=models.CharField(max_length=100)

    age=models.PositiveIntegerField()

    image=models.ImageField(upload_to="images",null=True)

    address=models.CharField(max_length=200)

    number=models.PositiveIntegerField()

    def __str__(self):

        return self.name