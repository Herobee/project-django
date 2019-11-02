from django.db import models
from django.urls import reverse

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
    item_quantity = models.IntegerField(default=0)
    on_sale = models.BooleanField(default=True)
    read_count = models.IntegerField(null=False, default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("item:item-detail", kwargs={"item_idx": self.item_idx})
    