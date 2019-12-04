from django import forms
from .models import Board

class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [
            'board_title',
            'board_content',
            'usr_name',
        ]

class BoardAddForm(forms.ModelForm):
    board_title = forms.CharField(
        label = ('Board Title'),
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'Board Title'
            }
        )
    )
    board_content = forms.CharField(
        label = ('Content for Board'),
        required = True,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Content..'
            }
        )
    )
    class Meta:
        model = Board
        fields = [
            'board_title',
            'board_content',
        ]
    def save(self, **kwargs):
        post = super().save(commit=False)
        post.usr_name = kwargs.get('usr_name',None)
        post.save()
        print('saved!')
        pass