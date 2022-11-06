from sqlite3 import Row
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label="Product Title", widget=forms.TextInput)
    description = forms.CharField(required=False, widget=forms.Textarea(
            attrs={ "class" : "my-txtarea spx1", "rows" : 20, "placeholder" : "Description" }
        )
    )
    price = forms.DecimalField(initial=199.99)