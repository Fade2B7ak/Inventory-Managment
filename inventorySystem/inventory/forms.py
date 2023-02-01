from django.forms import ModelForm
from .models import Inventory


class AddProductsForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemClass', 'name', 'model', 'quantity', 'price']


class UpdateProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemClass', 'name', 'model', 'quantity', 'price']
