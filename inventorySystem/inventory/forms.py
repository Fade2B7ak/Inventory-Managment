from django.forms import ModelForm
from .models import Inventory, User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password


class AddProductsForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemClass', 'name', 'model', 'quantity', 'price']


class UpdateProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemClass', 'name', 'model', 'quantity', 'price']
