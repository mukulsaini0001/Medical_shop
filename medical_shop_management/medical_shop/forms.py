from django import forms
from .models import Dealer, Medicine, Employee, Customer, Purchase

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['name', 'address', 'phone', 'email']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'manufacturer', 'price', 'quantity']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'email', 'designation']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'email']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['medicine', 'dealer', 'employee', 'customer', 'quantity']
