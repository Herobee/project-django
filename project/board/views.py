from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View

from django.db.models import F

from .models import Board
from .forms import BoardModelForm, BoardAddForm

import math

# Create your views here.
class BoardObjectMixin(object):
    model = Board
    lookup = 'Board_idx'

    def get_idx(self):
        board_idx = self.kwargs.get('board_idx')
        return board_idx

    def get_object(self):
        board_idx = self.kwargs.get('board_idx')
        obj = None
        if board_idx is not None:
            obj = get_object_or_404(Board, board_idx=board_idx)
        return obj

class BoardListView(View):
    template_name = "board/board_list.html"
    queryset = Board.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request, **kwargs):
        max_page = math.ceil(self.queryset.count()/8)
        print(max_page)
        order_by = self.kwargs.get('order')
        print(order_by)
        p = (1-1)*5
        if not order_by:
            self.queryset = self.queryset.filter().order_by('-board_idx')[p:8]
        else:
            self.queryset = self.queryset.filter().order_by(order_by)[p:8]
        context = {"board_list": self.get_queryset(),"page_num":range(1, max_page+1)}
        print(context)
        return render(request, self.template_name, context)

def pageBtn(request):
    pass

class BoardAddView(View):
    template_name = "board/board_add.html"
    def get(self, request, *args, **kwargs):
        # GET
        print('BoardAddView', request.user.is_anonymous)
        if request.user.is_anonymous:
            print('anonymous User!')
            return redirect('user:login')
        form = BoardAddForm
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST
        form = BoardAddForm(request.POST)
        if form.is_valid():
            form.save(usr_name=request.user)
            form = BoardAddForm()
            return redirect('board:board-list')
        context = {"form": form}
        return render(request, self.template_name, context)

class BoardDetailView(BoardObjectMixin, View):
    template_name = "board/board_detail.html"
    queryset = Board.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwagrs):
        # GET Method
        self.queryset = self.queryset.filter(board_idx=self.get_idx()).update(
            read_count=F('read_count')+1)
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

def AddTagBtn():
    print('!!!')
    pass
