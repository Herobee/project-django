from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View

from .models import Cart
# from .forms import CartAddForm

class CartObjectMixin(object):
    model = Cart
    lookup = 'id'
    def get_idx(self):
        id = self.kwargs.get('id')
        return id

class CartListView(View):
    template_name = "cart/cart_list.html"
    queryset = Cart.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwagrs):
        # GET
        self.queryset = self.queryset.filter(usr_id=request.user)
        context = {'object_list':self.get_queryset(),}
        return render(request, self.template_name, context)

class CartDelete(CartObjectMixin, View):
    queryset = Cart.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        #GET
        context = {'object':self.get_idx()}
        self.queryset = self.queryset.filter(id=self.get_idx()).delete()
        return redirect('cart:cart-list')
    
