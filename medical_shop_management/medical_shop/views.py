from django.shortcuts import render, redirect
from .models import Dealer, Medicine, Employee, Customer, Purchase
from .forms import DealerForm, MedicineForm, EmployeeForm, CustomerForm, PurchaseForm

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'dealer/dealer_list.html', {'dealers': dealers})

def add_dealer(request):
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dealer_list')
    else:
        form = DealerForm()
    return render(request, 'dealer/add_dealer.html', {'form': form})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine/medicine_list.html', {'medicines': medicines})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicine/add_medicine.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase/purchase_list.html', {'purchases': purchases})

def new_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'purchase/new_purchase.html', {'form': form})

    