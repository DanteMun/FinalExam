from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'number', 'address', 'about', 'photo1', 'photo2', 'photo3']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message', 'photo']