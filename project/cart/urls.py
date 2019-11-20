from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartListView.as_view(), name='cart-list'),
    # path('cartAdd', views.CartAddView.as_view(), name='cart-add'),
    path('<int:id>/cartDelete/', views.CartDelete.as_view(), name='cart-delete'),
]
