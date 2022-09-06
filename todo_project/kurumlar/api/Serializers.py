from pyexpat import model
from xml.dom import UserDataHandler
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from kurumlar.models import Kitaplar,Yorum,Kuruluslar
from django.contrib.auth.models import User




class KurulusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kuruluslar
        fields='__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    model=User
    fields = ('id','username','password','email','first_name','last_name')
    write_only_fields=('password',)
    read_only_fields=('id',)

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user