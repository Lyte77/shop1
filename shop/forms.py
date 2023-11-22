from django import forms
from .models import Product, Category
from django.contrib.auth.models import User

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','description','image','price']
        widgets = {
            'image':forms.FileInput(attrs={
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].queryset = Category.objects.all()


