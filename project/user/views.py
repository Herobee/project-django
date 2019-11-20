from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View

from .models import MyUser
from .forms import MyUserModelForm, MyLoginForm, MyUserCreateForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

class UserObjectMixin(object):
    model = MyUser
    lookup = 'usr_id'
    def get_object(self):
        usr_id = self.kwargs.get('usr_id')
        obj = None
        if usr_id is not None:
            obj = get_object_or_404(MyUser, usr_id = usr_id)
        return obj

class SignupView(View):
    template_name = "user/signup.html"
    def get(self, request, *args, **kwargs):
        #GET Method
        form = MyUserCreateForm()
        context = {"form" : form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        #POST Method
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form = MyUserCreateForm()
            return redirect('user:login')
        context = {"form" : form}
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = "user/login.html"
    def get(self, request):
        # GET METHOD
        form = MyLoginForm()
        context = {"form" : form}
        return render(request, self.template_name, context)
    def post(self, request):
        # POST
        form = MyLoginForm(request.POST)
        usr_id = request.POST['usr_id']
        password = request.POST['password']
        user = authenticate(usr_id=usr_id, password=password)
        if user is not None:
            if user.is_active:
                print('login!!!!!!!!!!!!!')
                login(request, user)
                return redirect('home')
        else:
            messages.warning(request, 'Try Again')
            return HttpResponse('')
        return render(request, self.template_name)
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        #GET
        logout(request)
        return redirect('home')

class DeleteUser(View):
    def get(self, request, *args, **kwargs):
        #GET
        request.user.delete()
        return redirect('home')

class UserListView(View):
    template_name = "user/user_list.html"
    queryset = MyUser.objects.all().order_by('-reg_date')
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter()
        context = {"object_list" : self.get_queryset()}
        return render(request, self.template_name, context)

class UserDetailView(UserObjectMixin, View):
    template_name = "user/user_detail.html"
    def get(self, request, usr_id=None, *args, **kwargs):
        #GET Method
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)