from django.contrib.auth.models import User, Group
from quickstart.models import Task, TaskGroup
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskGroup
        fields = "__all__"
