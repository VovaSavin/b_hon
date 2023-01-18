from django.db import models
import uuid


# Create your models here.


class UsersOrder(models.Model):
    """
    Users order
    """
    name_order = models.CharField(max_length=255, verbose_name="Замовлення")
    phone_user = models.CharField(max_length=15, verbose_name="Номер користувача")
    individual_key = models.UUIDField(
        max_length=15,
        verbose_name="Ідентифікатор замовлення",
        default=uuid.uuid4,
        unique=True,
    )
    comment = models.TextField(verbose_name="Коментар до замовлення", blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_order

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


class Goods(models.Model):
    """
    All goods
    """
    name_good = models.CharField(max_length=255, verbose_name="Товари")
    description = models.TextField(verbose_name="Опис товару")
    image = models.TextField(verbose_name="Посилання на зображення")
    price_from = models.SmallIntegerField(verbose_name="Ціна від", blank=True, null=True)
    if_show = models.BooleanField(verbose_name="Показувати на сайті", default=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.name_good

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


class About(models.Model):
    """Simple text for other description info"""

    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(verbose_name="Текст")
    picture = models.TextField(
        verbose_name="Посилання на фото", blank=True, null=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Загальне"
        verbose_name_plural = "Загальні"


class Contacts(models.Model):
    """Контакти"""

    name = models.CharField(max_length=100, verbose_name="Ваше ім'я")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    email = models.EmailField()
    our_address = models.TextField(default="", blank=True, null=True, verbose_name="Ваша адреса")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"
