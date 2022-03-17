from unicodedata import category
from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category
# Create your views here.
def store(request, c_slug=None):
    categories =None
    products = None
    
    if c_slug != None: # slug category path
        categories = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {'products': products, 'product_count':product_count,}
    return render(request, 'store/store.html', context)


def product_detail(request, c_slug, p_slug):
    try:
        single_product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e: 
        raise e
    context = {'single_product':single_product, }    
    return render(request, 'store/product_detail.html', context)