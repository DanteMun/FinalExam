from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message', 'photo']