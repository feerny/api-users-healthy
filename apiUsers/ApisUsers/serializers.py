from dataclasses import field
from rest_framework import serializers
from ApisUsers.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
            'email',
            'password'
        )