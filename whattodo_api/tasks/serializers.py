from django.contrib.auth.models import User

from rest_framework import serializers

from tasks.models import Task, Status, Priority


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ["id", "username"]

class StatusSerializer(serializers.ModelSerializer):
    """Serializer for Status listing"""
    class Meta:
        model = Status
        fields = "__all__"


class PrioritySerializer(serializers.ModelSerializer):
    """Serializer for Priority listing"""
    class Meta:
        model = Priority
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    """Serializer for Task listing"""
    status = StatusSerializer(many=False)
    priority = PrioritySerializer(many=False)
    created_by = UserSerializer(many=False)

    class Meta:
        model = Task
        fields = ["id", "summary", "status", "priority", "created_by", "creation_date"]


class TaskDetailSerializer(serializers.ModelSerializer):
    """Serializer for Task details"""
    status = StatusSerializer(many=False, read_only=True)
    priority = PrioritySerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        status = Status.objects.get(name="To Do")
        priority = self.context.get("priority")
        current_user = self.context.get("user")
        return Task.objects.create(
            status=status,
            priority=priority,
            created_by=current_user,
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.status = self.context.get("status")
        instance.priority = self.context.get("priority")
        instance.summary = validated_data.get("summary")
        instance.detailed_description = validated_data.get("detailed_description")
        instance.definition_of_done = validated_data.get("definition_of_done")
        instance.save()
        return instance

