from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
	class Meta:
        model = Product
		fields = ['Product_description','Cost']