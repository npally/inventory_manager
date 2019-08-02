from django.forms import ModelForm
from .models import Product

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['price', 'quantity']

class LessProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']
