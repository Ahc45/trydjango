from re import T
from .models import Product
from django import forms

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class rawProductForm(forms.Form):
    title = forms.CharField(max_length=20)
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class" : "form-control",
                                "rows" : '5'
                            }
                        )
    )
    price = forms.CharField(required=False,  widget=forms.TextInput(
                            attrs={
                                "class" : "form-control",
                                "type": "number",
                                "aria-describedby" : "id_price"
                            }
                        ))


class editProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
