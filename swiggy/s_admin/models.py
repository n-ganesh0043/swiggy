from django.db import models

# Create your models here.
class AdminLoginModel(models.Model):
    username=models.CharField(unique=True,max_length=20)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()

class Statemodel(models.Model):
    state_no=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.state_name

class Citymodel(models.Model):
    city_no=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=30)
    state=models.ForeignKey(Statemodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name

class Areamodel(models.Model):
    area_no=models.AutoField(primary_key=True)
    area_name=models.CharField(max_length=40)
    city=models.ForeignKey(Citymodel,on_delete=models.CASCADE)