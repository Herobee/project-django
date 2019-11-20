from django.db import models
from django.urls import reverse
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser, PermissionsMixin)


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, usr_id, usr_name, usr_email, usr_phone, password=None):
        if not usr_id:
            raise ValueError('must have User ID!!')
        user = self.model(
            usr_id = usr_id,
            usr_name = usr_name,
            usr_email = self.normalize_email(usr_email),
            usr_phone = usr_phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usr_id, usr_name, usr_email, usr_phone, password):
        user = self.create_user(
            usr_id = usr_id,
            usr_name = usr_name,
            usr_email = self.normalize_email(usr_email),
            usr_phone = usr_phone,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()

    usr_id = models.CharField(max_length=45, primary_key=True)
    usr_name = models.CharField(max_length=45, null=False, unique=True)
    usr_email = models.CharField(max_length=45, null=False, unique=True)
    usr_phone = models.CharField(max_length=45, null=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'usr_id'
    REQUIRED_FIELDS = ['usr_name','usr_email','usr_phone']

    class Meta:
        ordering = ['-reg_date',]

    def __str__(self):
        return self.usr_id
    
    def get_absolute_url(self):
        return reverse("user:user-detail", kwargs={"usr_id": self.usr_id})

# class Basket(models.Model):
#     item_idx = models.ForeignKey(Item, default='', on_delete=models.CASCADE)
#     usr_id = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE)
#     item_count = models.IntegerField(null = False, default=1)
#     add_date = models.DateTimeField(auto_now_add=True)
#     def __str(self):
#         return self.usr_id,self.item_idx