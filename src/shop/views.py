from django.shortcuts import render, get_object_or_404

from shop.models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    

    template_name = 'shop/product/list.html'
    context = {'category': category,
                'categories': categories,
                'products': products}

    return render(request, template_name, context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)

    cart_product_form = CartAddProductForm()

    template_name = 'shop/product/detail.html'
    context = {'product': product,
                'cart_product_form': cart_product_form}

    return render(request, template_name, context)