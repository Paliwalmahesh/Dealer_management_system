from django.db import models


# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_description=models.TextField()
    Cost = models.FloatField()
    def __str__(self):
        return self.Product_description



