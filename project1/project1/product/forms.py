from django import forms
# from django.forms.models import inlineformset_factory

from .models import Buyer, Product

# ProductFormSet = inlineformset_factory(Buyer, Product, exclude=('buyer',))

class BuyerForm(forms.ModelForm):
	class Meta:
		model = Buyer
		exclude = ('invoice_date', 'invoice_no')

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ('buyer',)





