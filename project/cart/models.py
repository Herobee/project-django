from django.db import models
from django.urls import reverse

from user.models import MyUser
from item.models import Item

# Create your models here.
class Cart(models.Model):
    item_idx = models.ForeignKey(Item, default='', on_delete=models.CASCADE)
    usr_id = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)
    item_count = models.IntegerField(null = False, default=1)
    add_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-add_date',]
    def __str(self):
        return self.usr_id,self.item_idx