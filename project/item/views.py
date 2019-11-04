from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from .models import Item
from .forms import ItemModelForm

# Create your views here.
class ItemObjectMixin(object):
    model = Item
    lookup = 'item_idx'
    def get_object(self):
        item_idx = self.kwargs.get('item_idx')
        obj = None
        if item_idx is not None:
            obj = get_object_or_404(Item, item_idx = item_idx)
        return obj

class ItemListView(View):
    template_name = "item/item_list.html"
    queryset = Item.objects.all().order_by('item_idx')
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)

class ItemAddView(View):
    template_name = "item/item_add.html"
    def get(self, request, *args, **kwargs):
        #GET
        form = ItemModelForm
        context = {"form" : form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        #POST
        form = ItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ItemModelForm()
            return redirect('home')
        context = {"form": form}
        return render(request, self.template_name, context)

class ItemDetailView(ItemObjectMixin, View):
    template_name = "item/item_detail.html"
    def get(self, request, item_idx=None, *args, **kwargs):
        #GET Method
        context = {'object': self.get_object()}
        print(context)
        return render(request, self.template_name, context)

class ItemBuyView(ItemObjectMixin, View):
    template_name = "item/item_buy.html"
    def get(self, request, item_idx=None, *args, **kwargs):
        #GET Method
        context = {'object': self.get_object()}
        print(context)
        return render(request, self.template_name, context)

class ItemAddBasket(ItemObjectMixin, View):
    def get(self, request, item_idx=None, *args, **kwargs):
        print('---- Add to Basket  ---------')
        context = {'object': self.get_object()}
        return redirect('home')