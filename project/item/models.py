from django.db import models
from django.urls import reverse
from django.conf import settings
from user.models import MyUser

# Create your models here.
class Item(models.Model):
    ITEM_CATEGORIES = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
        (5, 'E'),
    )

    item_idx = models.AutoField(primary_key=True)
    item_category = models.IntegerField(null=False, default=1, choices=ITEM_CATEGORIES)
    item_name = models.CharField(max_length=45, null=False)
    item_content = models.TextField(blank = False, null=False)
    item_price = models.IntegerField(null=False)
    item_quantity = models.IntegerField(default=1)
    usr_name = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=True)
    read_count = models.IntegerField(null=False, default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("item:item-detail", kwargs={"item_idx": self.item_idx})
    
# class Basket(models.Model):
#     usr_id = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)
#     item_idx = models.ForeignKey(Item, default='', on_delete=models.CASCADE)
#     item_count = models.IntegerField(null = False, default=1)
#     add_date = models.DateTimeField(auto_now_add=True)
#     def __str(self):
#         return self.usr_id,self.item_idx
