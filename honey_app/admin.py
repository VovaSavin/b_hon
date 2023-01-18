from django.contrib import admin
from .models import UsersOrder, Goods, About, Contacts


# Register your models here.


@admin.register(UsersOrder)
class UsersOrderAdmin(admin.ModelAdmin):
    list_display = ["name_order", "phone_user", "date_order", ]
    list_filter = ["phone_user", ]


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name_good", "price_from", "if_show", ]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name", "date", ]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "date", ]
