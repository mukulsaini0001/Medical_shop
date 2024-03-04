from django.contrib import admin
from .models import Dealer,Medicine,Employee,Customer,Purchase
# Register your models here.

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','email')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'quantity')

    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','email','designation')
    
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('medicine','dealer','employee','customer','quantity','purchase_date')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','email')