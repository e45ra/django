from django.contrib import admin
from .models import Cage,  Store,  PersonData, Drug, Stores


@admin.register(Cage)
class CageAdmin(admin.ModelAdmin):
    list_display = ['drugs', 'submit_date', 'price_main', 'amount', 'cage_number']
    
@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = ['store', 'name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['drugs', 'submit_date', 'price_main', 'amount', 'store_number']
     

@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_name', 'date', 'phone_number']
    
@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['gtn', 'lot', 'generic_name', 'name']
    
