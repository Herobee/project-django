from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('delete/', views.DeleteUser.as_view(), name='delete-user'),
    path('userlist/', views.UserListView.as_view(), name='user-list'),
    path('detail/<str:usr_id>', views.UserDetailView.as_view(), name='user-detail'),
]
