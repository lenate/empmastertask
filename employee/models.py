from django.db import models



class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Phone=models.IntegerField(default=35354365)
    Email=models.EmailField(max_length=254)
    Image = models.ImageField(upload_to='gallery',default='')