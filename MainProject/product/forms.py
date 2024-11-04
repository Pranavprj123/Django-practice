from django.forms import ModelForm
from .models import Brand,Product


class BrandCreationForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        field_order = [
            'name',
            'logo',
            'origin',
            'tagline',
            'types',
            'since',
        ]

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        field_order = [
            'name',
            'price_inclusive',
            'brand',
            'description',
        ]
