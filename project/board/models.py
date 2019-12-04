from django.db import models
from django.urls import reverse
from django.conf import settings
from user.models import MyUser

# Create your models here.
class Board(models.Model):
    board_idx = models.AutoField(primary_key=True)
    board_title = models.CharField(max_length=45, null=False, blank=False)
    board_content = models.TextField(null=False, blank=False)
    usr_name = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)
    read_count = models.IntegerField(null=False, default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.board_title
    
    def get_absolute_url(self):
        return reverse("board:board-detail", kwargs={"board_idx": self.board_idx})
    