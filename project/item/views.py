from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from django.db.models import F

from .models import Item
from cart.models import Cart
from .forms import ItemModelForm, ItemAddForm
from cart.forms import CartAddForm

# Create your views here.


class ItemObjectMixin(object):
    model = Item
    lookup = 'item_idx'

    def get_idx(self):
        item_idx = self.kwargs.get('item_idx')
        return item_idx

    def get_object(self):
        item_idx = self.kwargs.get('item_idx')
        obj = None
        if item_idx is not None:
            obj = get_object_or_404(Item, item_idx=item_idx)
        return obj
    def get_count(self):
        item_count = self.kwargs.get('item_count')
        return item_count

class ItemCategoryChoice(object):
    model = Item
    lookup = 'item_idx'
    

class ItemListView(View):
    template_name = "item/item_list.html"
    queryset = Item.objects.all().order_by('-item_idx')
    def get_queryset(self):
        return self.queryset
    def get(self, request):
        page = 1
        self.queryset = self.queryset.filter()
        context = {
            "object_list": self.get_queryset(),
        }
        print(len(context["object_list"]))
        l = len(context["object_list"])
        if l / 12 > 1:
            page += 1
        context.update({"page":range(1,page+1)})
        
        return render(request, self.template_name, context)


class ItemAddView(View):
    template_name = "item/item_add.html"
    def get(self, request, *args, **kwargs):
        # GET
        print('ItemAddView', request.user.is_anonymous)
        if request.user.is_anonymous:
            return redirect('user:login')
        form = ItemAddForm
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST
        form = ItemAddForm(request.POST)
        if form.is_valid():
            form.save(usr_name=request.user)
            form = ItemAddForm()
            print('success!!!')
            return redirect('item:item-list')
        context = {"form": form}
        return render(request, self.template_name, context)


class ItemDetailView(ItemObjectMixin, View):
    template_name = "item/item_detail.html"
    qs = Item.objects.all()

    def get_queryset(self):
        return self.qs

    def get(self, request, item_idx=None, *args, **kwargs):
        # GET Method
        self.qs = self.qs.filter(item_idx=self.get_idx()).update(
            read_count=F('read_count')+1)
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

class ItemBuyView(ItemObjectMixin, View):
    template_name = "item/item_buy.html"
    queryset = Cart.objects.all()

    def get_queryset(self):
        return self.queryset
    def get(self, request, item_idx=None, *args, **kwargs):
        # GET Method
        form = CartAddForm()
        # form.save(usr_id=request.user, item_idx=self.get_object())
        self.queryset = self.queryset.filter(usr_id=request.user)
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class ItemAddCart(ItemObjectMixin, View):

    def get(self, request, item_idx=None, *args, **kwargs):
        context = {'object': self.get_object(), 'item_count':self.get_count()}
        print(context)
        
        form = CartAddForm()
        form.save(usr_id=request.user, item_idx=self.get_object())
        return redirect('cart:cart-list')

class TestAction(ItemObjectMixin, View):
    template_name = "item/item_detail.html"
    def get(self, request, item_idx=None,item_count=None, *args, **kwargs):
        print(request)
        print(item_idx)
        print(item_count)
        print(kwargs)
        return render(request, self.template_name)