from django.urls import path
from . import views

urlpatterns = [
    # URLs for dealers
    path('dealers', views.dealer_list),
    path('add_dealer', views.add_dealer),
    
    # URLs for medicines
    path('medicines', views.medicine_list),
    path('add_medicine', views.add_medicine),

    # URLs for employees
    path('employees', views.employee_list),
    path('add_employee', views.add_employee),

    # URLs for customers
    path('customers', views.customer_list),
    path('add_customer', views.add_customer),

    # URLs for purchases
    path('purchases', views.purchase_list),
    path('new_purchase', views.new_purchase),
]