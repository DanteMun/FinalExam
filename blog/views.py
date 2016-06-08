from django.shortcuts import render, get_object_or_404
from .models import Category, Shop

def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'category_list' : category_list,
        })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {
        'category' : category,
        })

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop' : shop,
        })
