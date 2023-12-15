from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Variant, Product,ProductImage,ProductVariant,ProductVariantPrice


class AddProduct(forms.ModelForm):
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"title", "class":"form-control"}), label="")
	
	
	class Meta:
		model = Product
		exclude = ("user",)
