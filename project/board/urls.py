from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('board-list/', views.BoardListView.as_view(), name='board-list'),
    # path('board-list/<int:num>', views.BoardListView.as_view(), name='board-list'),
    path('board-list/<str:order>', views.BoardListView.as_view(), name='board-list'),
    path('board-add/', views.BoardAddView.as_view(), name='board-add'),
    path('board-detail/<int:board_idx>', views.BoardDetailView.as_view(), name='board-detail'),
    path('AddTagBtn', views.AddTagBtn, name='add-tag'),
    # path('board-number/<int:int>', views.pageBtn, name="board-number"),
]
