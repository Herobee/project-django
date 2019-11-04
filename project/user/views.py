from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from .models import User
from .forms import UserModelForm, LoginForm

class UserObjectMixin(object):
    model = User
    lookup = 'usr_id'
    def get_object(self):
        usr_id = self.kwargs.get('usr_id')
        obj = None
        if usr_id is not None:
            obj = get_object_or_404(User, usr_id = usr_id)
        return obj

class SignupView(View):
    template_name = "user/signup.html"
    def get(self, request, *args, **kwargs):
        #GET Method
        form = UserModelForm()
        context = {"form" : form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        #POST Method
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserModelForm()
            return redirect('home')
        context = {"form" : form}
        return render(request, self.template_name, context)
class LoginView(View):
    template_name = "user/login.html"
    def get(self, request, *args, **kwargs):
        # GET METHOD
        form = LoginForm()
        context = {"form" : form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        # POST
        form = LoginForm(request.POST)
        usr_id = request.POST['usr_id']
        usr_pwd = request.POST['usr_pwd']
        print(usr_id)
        print(usr_pwd)
        return render(request, self.template_name)
        
class LogoutView(View):
    pass

class UserListView(View):
    template_name = "user/user_list.html"
    queryset = User.objects.all().order_by('-reg_date')
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        context = {"object_list" : self.get_queryset()}
        return render(request, self.template_name, context)

class UserDetailView(UserObjectMixin, View):
    template_name = "user/user_detail.html"
    def get(self, request, usr_id=None, *args, **kwargs):
        #GET Method
        context = {'object': self.get_object()}
        print(context)
        return render(request, self.template_name, context)
