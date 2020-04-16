from django.db import models
from s_admin.models import Areamodel,RestaurantType

class Restaurantmodel(models.Model):
    restro_id=models.AutoField(primary_key=True)
    restro_name=models.CharField(unique=True,max_length=40)
    restro_contact_no=models.IntegerField(unique=True)
    restro_email=models.EmailField(unique=True)
    restro_area=models.ForeignKey(Areamodel,on_delete=models.CASCADE)
    restro_type=models.ForeignKey(RestaurantType,on_delete=models.CASCADE)
    restro_password=models.CharField(max_length=20)
    restro_otp=models.IntegerField()
    restro_status=models.CharField(max_length=20)

