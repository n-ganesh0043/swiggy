from django import forms
from .models import Restaurantmodel
class Restaurantform(forms.ModelForm):
    restro_password=forms.CharField(max_length=20,widget=forms.PasswordInput,label='PASSWORD')
    class Meta:
        model=Restaurantmodel
        fields="__all__"
        exclude=('restro_otp','restro_status','restro_id')
        labels={'restro_name':'RESTAURANT NAME','restro_contact_no':'CONTACT NO','restro_area':'RESTAURANT AREA','restro_type':'RESTAURANT TYPE','restro_email':'EMAIL'}