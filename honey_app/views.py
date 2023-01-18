from .models import UsersOrder, Goods, About, Contacts
from .serializers import UsersOrderSerializer, GoodsSerializer, ListContactsSerializer, ListAboutSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView


# Create your views here.

class UserOrderViews(ListCreateAPIView):
    """
    Show and create users order
    """

    queryset = UsersOrder.objects.all()
    serializer_class = UsersOrderSerializer


class GoodsListApi(ListAPIView):
    """
    Show all goods
    """
    queryset = Goods.objects.filter(if_show=True)
    serializer_class = GoodsSerializer


class AboutListView(ListAPIView):
    """For display about page"""

    queryset = About.objects.all().order_by("id")
    serializer_class = ListAboutSerializer


class ContactsListView(ListAPIView):
    """For display contacts"""

    queryset = Contacts.objects.all()
    serializer_class = ListContactsSerializer
