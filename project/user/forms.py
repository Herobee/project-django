from django import forms
from .models import MyUser, MyUserManager

# class UserModelForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = [
#             'usr_id',
#             'password',
#             'usr_name',
#             'usr_email',
#             'usr_phone',
#         ]
        
#         def clean_usr_id(self):
#             usr_id = self.cleaned_data.get('usr_id')
#             return usr_id

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = [
#             'usr_id',
#             'password',
#         ]
class MyUserModelForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields=[
            'usr_id',
            'password',
            'usr_name',
            'usr_email',
            'usr_phone',
        ]
        def clean_usr_id(self):
            usr_id = self.cleaned_data.get('usr_id')
            return usr_id

class MyUserCreateForm(forms.ModelForm):
    usr_id = forms.CharField(
        label= ('USER ID'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER ID',
            }
        )
    )
    password1 = forms.CharField(
        label= ('USER PassWord'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER PassWord',
            }
        )
    )
    password2 = forms.CharField(
        label= ('USER PassWord'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm USER PassWord',
            }
        )
    )
    usr_name = forms.CharField(
        label= ('USER NickName'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER NickName',
            }
        )
    )
    usr_email = forms.EmailField(
        label= ('USER Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER Email',
            }
        )
    )
    usr_phone = forms.CharField(
        label= ('USER Phone Number'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER Phone Number',
            }
        )
    )

    class Meta:
        model = MyUser
        fields = ('usr_id','usr_name','usr_phone')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print('password1--------->', password1)
        print('password2--------->', password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords dont matched!!")
        return password2
    def save(self, commit=True):
        user = super(MyUserCreateForm, self).save(commit=False)
        user.usr_email = MyUserManager.normalize_email(self.cleaned_data['usr_email'])
        user.set_password(self.cleaned_data["password1"])
        print('user--------------')
        print(user)
        if commit:
            user.save()
        return user


class MyLoginForm(forms.ModelForm):
    usr_id = forms.CharField(
        label= ('USER ID'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER ID',
            }
        )
    )
    password = forms.CharField(
        label= ('USER PassWord'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'USER PassWord',
            }
        )
    )
    class Meta:
        model = MyUser
        fields = ('usr_id', 'password',)
        
    def clean_usr_id(self):
            usr_id = self.cleaned_data.get('usr_id')
            return usr_id
    