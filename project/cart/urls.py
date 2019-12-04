from django.urls import path
from . import views
from item import views as ItemView

app_name = 'cart'
urlpatterns = [
    path('', views.CartListView.as_view(), name='cart-list'),
    # path('cartAdd', views.CartAddView.as_view(), name='cart-add'),
    path('<int:id>/cartDelete/', views.CartDelete.as_view(), name='cart-delete'),
    # path('<int:item_idx_id>/buy', ItemView.ItemBuyView.as_view(), name='item-buy'),
]
