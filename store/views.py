from django.shortcuts import render
from .models import Category, Product



def homepage(request):
    all_categories = Category.objects.all()
    male_products = Product.objects.filter(category=1)
    female_products = Product.objects.filter(category=2)
    context = {"all_categories": all_categories,
               "male_products": male_products,
               "female_products": female_products}
    return render(request, "store/index.html", context)

# Create your views here.
