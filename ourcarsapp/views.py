from django.views import generic
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View, ListView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template import defaultfilters
import operator
from .models import Cars, Service, CarsImage
from .forms import UserForm, ServiceForm, CarsPhoto, BigPhotos


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'ourcarsapp/login.html')
    else:
        cars = Cars.objects.filter(user=request.user)     
        query = request.GET.get("q")
        if query:
            cars = cars.filter(
                Q(car_make__icontains=query) |
                Q(car_model__icontains=query)
           ).distinct()
            return render(request, 'ourcarsapp/index.html', {
                'cars': cars,
            })
        else:
            return render(request, 'ourcarsapp/index.html', {'cars': cars})
 
def allmycars(request):
    if not request.user.is_authenticated:
        return render(request, 'ourcarsapp/login.html')
    else:
        cars = Cars.objects.filter(user=request.user)     
        query = request.GET.get("q")
        if query:
            cars = cars.filter(
                Q(car_make__icontains=query) |
                Q(car_model__icontains=query)
           ).distinct()
            return render(request, 'ourcarsapp/all_my_cars.html', {
                'cars': cars,
            })
        else:
            return render(request, 'ourcarsapp/all_my_cars.html', {'cars': cars})

def big_photos(request, cars_id):
    form = BigPhotos(request.POST or None, request.FILES or None)
    cars = get_object_or_404(Cars, pk=cars_id)

    context = {
        'cars': cars,
        'form': form,
    }
    return render(request, 'ourcarsapp/big_photos.html', context)

class DetailView(generic.DetailView):
    model = Cars
    template_name = 'ourcarsapp/detail.html'


class CarsCreate(CreateView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    model = Cars
    fields = ['car_make', 'car_model', 'year_made', 'current_car', 'rego', 'kms_bought', 'kms_sold',
              'nickname', 'comments', 'cars_logo', 'when_sold', 'user']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(CarsCreate, self).form_valid(form)


class CarsUpdate (UpdateView):
    model = Cars
    fields = ['user', 'car_make', 'car_model', 'year_made', 'current_car', 'rego', 'kms_bought', 'kms_sold', 'nickname', 'comments', 'cars_logo', 'when_sold', 'user']


class CarPhotosUpdate (UpdateView):
    model = CarsImage
    fields = ['cimage']
    success_url = reverse_lazy('ourcarsapp:all_my_cars')

       
class CarsDelete (LoginRequiredMixin, DeleteView): 
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cars

    
def service_delete(request, cars_id, service_id):
    cars = get_object_or_404(Cars, pk=cars_id)
    service = Service.objects.get(pk=service_id)
    service.delete()
    return render(request, 'ourcarsapp/detail.html', {'cars': cars})

    
def service_form(request, cars_id):
    form = ServiceForm(request.POST or None, request.FILES or None)
    cars = get_object_or_404(Cars, pk=cars_id)
    if form.is_valid():
        service = form.save(commit=False)
        service.cars = cars        
        service.save()
        return render(request, 'ourcarsapp/detail.html', {'cars': cars})
    context = {
        'cars': cars,
        'form': form,
    }
    return render(request, 'ourcarsapp/service_form.html', context)


def car_image(request, cars_id):
    form = CarsPhoto(request.POST or None, request.FILES or None)
    cars = get_object_or_404(Cars, pk=cars_id)
    if form.is_valid():
        cimage = form.save(commit=False)
        cimage.cars = cars
        cimage.save()
        return render(request, 'ourcarsapp/detail.html', {'cars': cars})
    context = {
        'cars': cars,
        'form': form,
    }
    return render(request, 'ourcarsapp/service_form.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'ourcarsapp/register.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('ourcarsapp:index')
            
        return render(request, self.template_name, {'form' : form}) 

  
class LoginView(View):
    form_class = UserForm
    template_name = 'ourcarsapp/login.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
    
            if user is not None:
                if user.is_active:
                    login(request, user)
    
                    return redirect('ourcarsapp:index')
                else:
                    return redirect('ourcarsapp:login')
            else:
                return redirect('ourcarsapp:login')

        return render(request, 'ourcarsapp:index')
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        form = UserForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, 'ourcarsapp/login.html', context)
    
    


  
                
                
