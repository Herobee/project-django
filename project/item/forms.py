from django import forms
from .models import Item

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_category',
            'item_name',
            'item_content',
            'item_price',
        ]
