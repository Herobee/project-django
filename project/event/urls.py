from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'event'
urlpatterns = [
    path('', views.EventIndexView.as_view(), name="event-index"),
    path('add/', views.AddProductView.as_view(), name="product-add"),
    path('list/',views.ProductListView.as_view(), name="product-list"),
    path('<int:product_idx>/detail/', views.ProductDetailView.as_view(), name="product-detail"),
]

if settings.DEBUG is True:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_URL)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)