from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Product, Category
from django.db.models import Q
from .forms import AddProductForm,EditProductForm
from django.urls import reverse_lazy

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy('shop:home')
    template_name = 'shop/add_products.html'

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductEditView(UpdateView):
    model = Product
    form_class = EditProductForm
    success_url = reverse_lazy('shop:home')
    template_name = 'shop/add_products.html'
    

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:home')

def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else Product.objects.all()
        categories = Category.objects.filter(name__icontains=query) if query else Category.objects.all()

        
    
    return render(request, 'shop/home.html',{
                                             'results':results,
                                             'categories':categories,
                                             'query':query})

# def categorey_search(request):
#     query = request.GET.get('q')
#     if query:
#         categories = Category.objects.filter(name__icontains=query)
#     else:
#         categories = Category.objects.all()
#     return render(request, 'shop/home.html',{'categories':categories})
