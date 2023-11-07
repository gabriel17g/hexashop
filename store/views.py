from django.shortcuts import render
from .models import Category
from django.contrib.auth.models import User


def homepage(request):
    all_categories = Category.objects.all()
    context = {"all_categories": all_categories}
    return render(request, "store/index.html", context)

# Create your views here.
