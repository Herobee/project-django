from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from django.db.models import F

from .models import Item
from .forms import ItemModelForm, ItemAddForm

# Create your views here.

class ItemObjectMixin(object):
    model = Item
    lookup = 'item_idx','item_quantity'

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
        item_count = self.kwargs.get('item_quantity')
        return item_count

class TestObject(object):
    model = Item
    lookup = 'item_quantity'

    def get_quantity(self):
        item_quantity=self.kwargs.get('item_quantity')
        return item_quantity
    

class ItemListView(View):
    template_name = "item/item_list.html"
    queryset = Item.objects.all().order_by('-item_idx')
    def get_queryset(self):
        return self.queryset
    def get(self, request):
        self.queryset = self.queryset.filter()
        context = {
            "object_list": self.get_queryset(),
        }
        return render(request, self.template_name, context)


class ItemAddView(View):
    template_name = "item/item_add.html"
    def get(self, request, *args, **kwargs):
        # GET
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