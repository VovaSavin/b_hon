from rest_framework import serializers
from .models import (
    UsersOrder,
    Goods,
    About,
    Contacts
)
from .service import get_me
import uuid


class GoodsSerializer(serializers.ModelSerializer):
    """
    Serialize UserOrder models
    """

    class Meta:
        model = Goods
        fields = "__all__"


class UsersOrderSerializer(serializers.ModelSerializer):
    """
    Serialize UserOrder models
    """

    def create(self, validated_data):
        validated_data['individual_key'] = uuid.uuid4()
        get_me(
            f"""
            Нове замовлення: \n {validated_data['name_order']}
            \nНомер замовника: \n +38{validated_data['phone_user']}
            \nКоментар до замовлення: \n {validated_data['comment']}
            """
        )
        instance = UsersOrder.objects.create(
            **validated_data
        )
        return instance

    class Meta:
        model = UsersOrder
        fields = "__all__"


class ListAboutSerializer(serializers.ModelSerializer):
    """Serializer for services"""

    class Meta:
        model = About
        fields = "__all__"


class ListContactsSerializer(serializers.ModelSerializer):
    """Serializer for services"""

    class Meta:
        model = Contacts
        fields = "__all__"
