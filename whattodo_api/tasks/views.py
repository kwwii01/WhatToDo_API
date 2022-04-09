from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task, Status, Priority
from tasks.serializers import (
    TaskListSerializer,
    StatusSerializer,
    PrioritySerializer,
    TaskDetailSerializer,
)


@api_view(["GET"])
def status_list(request):
    """List all statuses"""
    if request.method == "GET":
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def priority_list(request):
    """List all priorities"""
    if request.method == "GET":
        priorities = Priority.objects.all()
        serializer = PrioritySerializer(priorities, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def task_list(request):
    """List all tasks"""
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        priority = Priority.objects.get(id=request.data.get("priority_id"))
        serializer = TaskDetailSerializer(
            data=request.data,
            context={
                "user": request.user,
                "priority": priority,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)   


@api_view(["GET"])
def task_details(request, pk):
    """Details of specific task"""
    if request.method == "GET":
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task, many=False)
        return Response(serializer.data)
