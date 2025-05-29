from django.contrib import admin
from .models import Cars, Service, CarsImage
admin.site.register(Cars)
admin.site.register(Service)
admin.site.register(CarsImage)


class CarsImageInline(admin.TabularInline):
    model = CarsImage
    extra = 3


class CarsAdmin(admin.ModelAdmin):
    inlines = [ CarsImageInline, ]
