from django.urls import path
from . import views
    
app_name = 'item'
urlpatterns = [
    path('itemlist/', views.ItemListView.as_view(), name='item-list'),
    path('itemlist/<int:page_num>', views.ItemListView.as_view(), name='item-list'),
    path('itemAdd/', views.ItemAddView.as_view(), name='item-add'),
    path('detail/<int:item_idx>', views.ItemDetailView.as_view(), name='item-detail'),
]
