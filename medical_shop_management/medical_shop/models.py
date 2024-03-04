from django.db import models

# Create your models here.
class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length = 15)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
class Medicine(models.Model):
    name = models.CharField(max_length = 100)
    manufacturer = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length= 15)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete = models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return f"Purchase of {self.medicine.nam} by {self.customer.name}"
    