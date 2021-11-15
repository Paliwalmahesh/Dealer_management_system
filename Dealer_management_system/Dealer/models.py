from django.db import models
from administrator.models import Product
from django.contrib.auth.models import User

# Create your models here.
ORDER_CHOICES=(
    ('Pending','Pending'),
    ('viewed','viewed'),
    ('Send_back','Send_back'),
    ('Approved','Approved'),
    ('delivering','delivering'),
    ('delivered','delivered'),
    
)
class Order(models.Model):
    user_order=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User')
    order_id = models.AutoField(primary_key=True)
    Order_date_Time=models.DateTimeField(auto_now_add=True)
    Order_Status=models.CharField(choices = ORDER_CHOICES,max_length=10,default='Pending')
    cost=models.FloatField()
    def __str__(self):
        Order_id_n=str(self.order_id)
        return Order_id_n

class Product_in(models.Model):
    Product_in_def=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Product')
    order_in=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='Order')
    Product_in_id=models.AutoField(primary_key=True)
    Quantity=models.IntegerField(default=1)
    Total_cost=models.FloatField()
    def __str__(self):
        Product_in_idn =str(self.Product_in_id)
        return Product_in_idn
    

