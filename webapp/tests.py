from django.test import TestCase

# Create your tests here.

class student(models.Model):
    sid=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    lastname= models.CharField(max_length = 20)
    gender= models.CharField(max_length = 20)
    email= models.CharField(max_length = 20)
    phone= models.CharField(max_length = 20)
    department= models.CharField(max_length = 20)
    dateofbirth= models.DateField()
    address= models.TextField()