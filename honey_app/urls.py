from django.urls import path

from . import views

urlpatterns = [
    path("orders_all/", views.UserOrderViews.as_view(), name="orders"),
    path("goods_all/", views.GoodsListApi.as_view(), name="goods"),
    path("about/", views.AboutListView.as_view(), name="goods"),
    path("contacts/", views.ContactsListView.as_view(), name="goods"),
]
