from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline


class CarMakeAdmin(admin.ModelAdmin):
    fields = ["name", "description"]
    search_fields = ['name']


class CarModelAdmin(admin.ModelAdmin):
    fields = ["car_make", "name", "type", "year"]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)


admin.site.register(CarModel, CarModelAdmin)
