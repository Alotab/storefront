from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

# Overriding the djoser User create serializer so that,
# we can more options like first_name, last_name etc when creating a user

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta): # this inherits everything in the BaseUserCreateSerializer' Meta class
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


# using this serializer for the current user show other details of the user
class UserSerialzer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    