from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    usr_id = models.CharField(max_length=45, primary_key=True)
    usr_pwd = models.CharField(max_length=45, null=False)
    usr_name = models.CharField(max_length=45, null=False, unique=True)
    usr_email = models.CharField(max_length=45, null=False)
    usr_phone = models.CharField(max_length=45, null=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.usr_id
    
    def get_absolute_url(self):
        return reverse("user:user-detail", kwargs={"usr_id": self.usr_id})
