from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse


class Cars(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    car_make = models.CharField(max_length=250)
    car_model = models.CharField(max_length=250)
    year_made = models.CharField(max_length=20)
    kms_bought = models.CharField(max_length=100, blank=True)
    kms_sold = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=250, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    cars_logo = models.FileField()
    rego = models.CharField(max_length=10, blank=True)   
    when_sold = models.CharField(max_length=10, blank=True)
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    current_car = models.BooleanField(choices=BOOL_CHOICES, default=True)
    colour = models.CharField(max_length=20, blank=True)
    
    def get_absolute_url(self):
        return reverse('ourcarsapp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.car_make + ' - ' + self.car_model
   
    class Meta:
         ordering = ['-current_car', 'car_make']


class CarsImage(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    cimage = models.ImageField()

    def __str__(self):
        return str(self.cimage)


class Service(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    last_serv = models.DateField()
    next_serv = models.DateField()
    serv_by = models.CharField(max_length=20)
    serv_url = models.URLField(max_length=200, blank=True)
    serv_phone = models.CharField(max_length=20, blank=True)
    serv_details = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.serv_by
