from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Shop, Review
from .forms import CategoryForm, ShopForm, ReviewForm

def index(request):
    category_list = Category.objects.all()
    review_list = Review.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {
        'category_list' : category_list,
        'review_list' : review_list,
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

@login_required
def category_new(request):
    if request.method =="POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, '새로운 카테고리가 등록되었습니다.')
            return redirect(category)
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {
        'form': form,
        })

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method =="POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, '카테고리 정보가 수정되었습니다.')
            return redirect(category)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/category_form.html', {
        'form': form,
        })

@login_required
def shop_new(request):
    if request.method =="POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            messages.success(request, '새로운 가게가 등록되었습니다.')
            return redirect(shop)
    else:
        form = ShopForm()
    return render(request, 'blog/shop_form.html', {
        'form': form,
        })

@login_required
def shop_edit(request, pk):
    shop = get_object_or_404(Shop, pk=pk)

    if request.method =="POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.save()
            messages.success(request, '가게 정보가 수정되었습니다.')
            return redirect(shop)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'blog/shop_form.html', {
        'form': form,
        })

@login_required
def review_new(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.user = request.user
            review.save()
            messages.success(request, '새로운 리뷰가 등록되었습니다.')
            return redirect(shop)
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {
        'form' : form,
        })

@login_required
def review_edit(request, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            messages.success(request, '리뷰 내용이 수정되었습니다.')
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'blog/review_form.html', {
        'form' : form,
        })