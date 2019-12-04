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
            'usr_name',
        ]
class ItemAddForm(forms.ModelForm):

    item_category = forms.ChoiceField(
        label = ('Item Category'),
        choices = Item.ITEM_CATEGORIES,
        widget = forms.Select(
            attrs = {
                'class':'form-control',
            }
        )
    )
    item_name = forms.CharField(
        label = ('Item NAME'),
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Item Name',
            }
        )
    )
    item_content = forms.CharField(
        label = ('Content for Item '),
        required = True,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Content..'
            }
        )
    )
    item_price = forms.IntegerField(
        label = ('Item Price'),
        required = True,
        widget = forms.NumberInput(
            attrs= {
                'class' : 'form-control',
            }
        )
    )
    item_quantity = forms.IntegerField(
        label = ('Quantity of Item'),
        initial = 1,
        min_value= 1,
        widget = forms.NumberInput(
            attrs = {
                'class' : 'form-control',
            }
        )
    )
    class Meta:
        model = Item
        fields = [
            'item_name',
            'item_category',
            'item_content',
            'item_price',
            'item_quantity',
            # 'usr_name'
        ]
    def save(self, **kwargs):
        post = super().save(commit=False)
        post.usr_name = kwargs.get('usr_name',None)
        post.save()
        pass
