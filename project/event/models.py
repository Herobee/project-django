from django.db import models
from django.conf import settings
from user.models import MyUser

# Create your models here.

class Product(models.Model):
    product_idx = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, null=False, blank=False)
    product_img = models.ImageField(blank=True, upload_to="event/%Y/%m/%d")
    product_profile = models.ImageField(upload_to="event/profile")
    prouct_like = models.IntegerField(default = 0)
    usr_id = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.product_img)