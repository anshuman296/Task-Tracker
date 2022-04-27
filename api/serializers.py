from django.db.models import fields
from rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ('team_name', 'members')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'assigned')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'
