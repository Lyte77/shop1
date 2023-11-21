from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from .models import Product
from .forms import AddProductForm
from django.urls import reverse_lazy

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy('shop:home')
    template_name = 'shop/add_products.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:home')