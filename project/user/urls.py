from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('userlist/', views.UserListView.as_view(), name='user-list'),
    path('<str:usr_id>/detail', views.UserDetailView.as_view(), name='user-detail'),
]
