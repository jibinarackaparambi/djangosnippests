from django.contrib.auth.models import User
from django.db import transaction

from rest_framework import serializers

from myapp.models import Snippests,Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data.get('username', None),
            password=validated_data.get('password', None))
    


class TagSerializer(serializers.ModelSerializer):
     class Meta:
        model = Tag
        fields = "__all__"
       

class CreateSnippestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippests
        fields = ('title','user','tag', 'created_at')
       