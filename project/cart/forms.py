from django import forms
from .models import Cart
from item.models import Item

class CartAddForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'item_idx',
            'usr_id',
        ]
    def save(self, *args, **kwargs):
        print('??????????????????')
        post = super().save(commit=False)
        post.item_idx = kwargs.get('item_idx',None)
        post.usr_id = kwargs.get('usr_id',None)
        post.save()
        print('-------------------------------')
        print('Cart Added!')
        print('-------------------------------')
        pass