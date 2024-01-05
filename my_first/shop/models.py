from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    product_date=models.DateField()
    category=models.CharField(max_length=30, default="")
    cost=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pic=models.ImageField(upload_to="shop/images/", default="")
    
    def __str__(self):
     return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    
