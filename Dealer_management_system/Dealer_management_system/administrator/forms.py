from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['Product_description','Cost']
		widgets = {
			'Product_description' : forms.Textarea(attrs={'class':'form-control my-3 ','id':'floatingTextarea','style':'height: 100px'}),
		    'Cost':forms.NumberInput(attrs={'class':'form-control my-3'})
		} 


		#NumberInput