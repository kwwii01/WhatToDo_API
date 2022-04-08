from rest_framework import serializers

from tasks.models import Task


class StatusSerializer(serializers.Serializer):
    """Serializer for Status model"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=24)


class PrioritySerializer(serializers.Serializer):
    """Serializer for Priority model"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=24)


class TaskListSerializer(serializers.Serializer):
    """Serializer for Task model"""
    id = serializers.IntegerField(read_only=True)
    summary = serializers.CharField(max_length=128)
    status = serializers.SlugRelatedField(slug_field="name", read_only=True)
    priority = serializers.SlugRelatedField(slug_field="name", read_only=True)
    creation_date = serializers.DateTimeField()
