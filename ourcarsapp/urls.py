
from django.urls import include, re_path
#from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings

from .import views

app_name = 'ourcarsapp'


urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^allmycars$', views.allmycars, name='all_my_cars'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', views.CarsUpdate.as_view(), name ='cars-update'),
    re_path(r'^(?P<pk>[0-9]+)/carsimage_form/$', views.CarPhotosUpdate.as_view(), name ='carsphoto-update'),
    re_path(r'cars/add/$', views.CarsCreate.as_view(), name ='car-add'),
    re_path(r'^(?P<pk>[0-9]+)/cars-delete$', views.CarsDelete.as_view(), name ='cars-delete'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),
   # url(r'^(?P<cars_id>[0-9]+)/service_form/$', views.service_form, name='service_form'), Old way
    path('service_form/<cars_id>', views.service_form, name='service_form'), # New way for URLs
    re_path(r'^(?P<cars_id>[0-9]+)/car_image/$', views.car_image, name='car_image'),
    re_path(r'^(?P<cars_id>[0-9]+)/big_photos/$', views.big_photos, name='big_photos'),
    re_path(r'^(?P<cars_id>[0-9]+)/service_delete/(?P<service_id>[0-9]+)/$', views.service_delete, name ='service_delete'),
    re_path(r'^service_form/(?P<filter_by>[a-zA_Z]+)/$', views.service_form, name='service_form'),
    #url(r'^(?P<pk>[0-9]+)/service_form/$', views.ServiceForm.as_view(), name='service_form'),
  
  
]