from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('itemlist/', views.ItemListView.as_view(), name='item-list'),
    path('itemlist/<int:page_num>', views.ItemListView.as_view(), name='item-list'),
    path('itemAdd/', views.ItemAddView.as_view(), name='item-add'),
    path('<int:item_idx>/detail', views.ItemDetailView.as_view(), name='item-detail'),
    path('buy/', views.ItemBuyView.as_view(), name='item-buy'),
    path('<int:item_idx>/buy', views.ItemBuyView.as_view(), name='item-buy'),
    path('<int:item_idx>/add-basket', views.ItemAddCart.as_view(), name='item-add-basket'),
    path('<int:item_idx>/test', views.TestAction.as_view(), name='test'),
]
