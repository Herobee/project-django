from django import forms
from .models import Cart
from item.models import Item

class CartAddForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'item_idx',
            'usr_id',
            'item_count',
            # 'item_price',
        ]
    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        post.item_idx = kwargs.get('item_idx',None)
        post.usr_id = kwargs.get('usr_id',None)
        print(post.item_idx)
        print(post.usr_id)
        print(post.kwargs.get('item_count',None))
        post.item_count = kwargs.get('item_count',None)
        # post.item_price = kwargs.get('item_price',None)*kwargs.get('item_count',None)
        post.save()
        pass