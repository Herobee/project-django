from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_idx',
            'product_name',
            'product_img',
            # 'product_like',
            'usr_id',
        ]
class ProductAddForm(forms.ModelForm):
    product_name = forms.CharField(
        label = ('Product Name'),
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Product Name'
            }
        )
    )
    product_img = forms.ImageField()
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_img',
        ]
    def save(self, **kwargs):
        post = super().save(commit=False)
        post.usr_id = kwargs.get('usr_id', None)
        post.save()
        print('successed to Upload!')
        pass
