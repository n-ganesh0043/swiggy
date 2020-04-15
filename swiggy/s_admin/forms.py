from django import forms
from s_admin.models import Statemodel,Citymodel,Areamodel

class Stateform(forms.ModelForm):
    class Meta:
        model=Statemodel
        fields=('state_name',)

class Cityform(forms.ModelForm):
    class Meta:
        model=Citymodel
        fields="__all__"
        exclude=('city_no',)

class Areaform(forms.ModelForm):
    class Meta:
        model=Areamodel
        fields="__all__"
        exclude=('area_no',)