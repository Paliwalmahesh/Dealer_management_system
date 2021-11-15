from django.forms import ModelForm
from django import forms
from .models import Order,Product_in


class OrderForm(ModelForm):
	class Meta:
        model = Order
		fields = ['Order_Status']

class Product_inForm(ModelForm):
	class Meta:
        model = Product_in
		fields = ['Product_in_def','order_in','Quantity']