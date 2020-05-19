from operator import truediv

from django.db import models

class studentdetail(models.Model):
    sid=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    lastname= models.CharField(max_length = 20)
    gender= models.CharField(max_length = 20)
    email= models.CharField(max_length = 30)
    phone= models.CharField(max_length = 20)
    department= models.CharField(max_length = 20)
    dateofbirth= models.DateField()
    address= models.TextField()