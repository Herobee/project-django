from django import forms
from .models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'usr_id',
            'usr_pwd',
            'usr_name',
            'usr_email',
            'usr_phone',
        ]
        def clean_usr_id(self):
            usr_id = self.cleaned_data.get('usr_id')
            return usr_id