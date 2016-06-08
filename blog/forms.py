from django import forms
from .models import Category, Shop

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'

