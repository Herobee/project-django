from django.contrib import admin
from . import models

@admin.register(models.MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'usr_id',
        'usr_name',
        'usr_email',
        'usr_phone',
        'reg_date',
        'updated_date',
    )
    list_display_links = (
        'usr_id',
        'usr_name',
        'usr_email',
        'usr_phone',

    )