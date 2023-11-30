from django.urls import path, include
from . import views
from .views import ProductListView,ProductCreateView,ProductDeleteView,ProductEditView

app_name = 'shop'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('home/', ProductListView.as_view(), name='home'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(),name='edit'),
    path('search/', views.search_view, name='search'),
    
]