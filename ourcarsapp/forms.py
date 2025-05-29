from django.contrib.auth.models import User
from django import forms
from django.forms import DateField
from django.utils.html import format_html
from .models import Cars, Service, CarsImage


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        
class CarsForm(forms.ModelForm):
    
    class Meta:
        model = Cars
        fields = ['car_make', 'car_model', 'year_made', 'kms_bought', 'kms_sold', 'nickname', 'comments', 'cars_logo', 'rego', 'current_car', 'user']


class ServiceForm(forms.ModelForm):
    next_serv = DateField(input_formats=["%d/%m/%Y"])
    last_serv = DateField(input_formats=["%d/%m/%Y"])
       
    class Meta:
        model = Service
        fields = ['next_serv', 'serv_by', 'serv_url', 'serv_phone', 'serv_details', 'last_serv']


class CarsPhoto(forms.ModelForm):

    class Meta:
        model = CarsImage
        fields = ['cimage']


class BigPhotos(forms.ModelForm):

    class Meta:
        model = CarsImage
        fields = ['cimage']