from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import ProductAddForm
from .models import Product
# Create your views here.

class ProductObjectMixin(object):
    model = Product
    lookup = 'product_idx'
    def get_idx(self):
        product_idx = self.kwargs.get('product_idx')
        return product_idx
    def get_object(self):
        product_idx = self.kwargs.get('product_idx')
        obj = None
        if product_idx is not None:
            obj = get_object_or_404(Product, product_idx=product_idx)
        return obj


class EventIndexView(View):
    template_name = "event/event.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AddProductView(View):
    template_name = "event/product_upload.html"
    def get (self, request, *args, **kwargs):
        form = ProductAddForm
        context = {"form":form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = ProductAddForm(request.POST, request.FILES)
        print(request.user)
        print(request)
        if form.is_valid():
            form.save(usr_id=request.user)
            form = ProductAddForm()
            print(form)
            return redirect('event:event-index')
        context = {"form":form}
        return render(request, self.template_name, context)
class ProductListView(View):
    template_name = "event/product_list.html"
    queryset = Product.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request, **kwagrs):
        context = {"product":self.get_queryset().filter()}
        return render(request, self.template_name, context)
    
class ProductDetailView(ProductObjectMixin, View):
    template_name = "event/product_detail.html"
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        #GET METHDO
        self.queryset = self.queryset.filter(product_idx=self.get_idx())
        context = {'object':self.get_object()}
        print(context["object"])
        return render(request, self.template_name, context)
    