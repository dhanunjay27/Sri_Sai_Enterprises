from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    query = request.GET.get('q') or ''
    cat_slug = request.GET.get('category') or ''
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    if cat_slug:
        products = products.filter(category__slug=cat_slug)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'active_category': cat_slug,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    categories = Category.objects.all()
    return render(request, 'store/product_detail.html', {
        'product': product,
        'images': images,
        'categories': categories,
    })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})
