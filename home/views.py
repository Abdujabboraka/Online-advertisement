import random

from django.shortcuts import render, redirect
from .models import  Category, Ad
# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    ad = Ad.objects.all()
    colors = ['255, 206, 50', '58, 119, 255', '35, 229, 219', '255, 86, 54', '255, 246, 217', '206, 221, 255', '200, 248, 246', '255, 214, 201','255, 206, 50', '206, 221, 255', '200, 248, 246', '255, 214, 201']
    context = {
        'categories_with_colors': zip(categories, colors),
        'categories': categories,
        'ads': ad,
        'colors': colors,
    }
    return render(request, 'index.html', context)

def select_by_category(request, category_id):
    categories = Category.objects.all()
    ad = Ad.objects.filter(category=category_id)
    context = {'categories': categories, 'ads': ad}
    return render(request, 'all_posts.html', context)


def add_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        address = request.POST['address']
        phone = request.POST['phone']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        ad = Ad(name=name, description=description, image=image, price=price, address=address, phone=phone, category=category)
        ad.save()
        return redirect('homepage')
    context = {'categories': categories}
    return render(request, 'add_post.html', context)

def all_posts(request):
    categories = Category.objects.all()
    ad = Ad.objects.all()
    context = {'categories': categories, 'ads': ad}
    return render(request, 'all_posts.html', context)

def view_more(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ads = []
    for i in range(4):
        ads.append(random.choice(Ad.objects.all()))
    categories = Category.objects.all()
    context = {'ad': ad, 'categories': categories, 'ads': ads}
    return render(request, 'view_more.html', context)
