from django.shortcuts import render, get_object_or_404
from .models import Shop

def index(request):
    return render(request, 'blog/index.html')

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop' : shop,
        })
