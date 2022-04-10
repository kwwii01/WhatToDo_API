from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
def task_list(request):
    """List all tasks"""
    if request.method == "GET":
        tasks = Task.objects.filter(created_by=request.user)
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
    # Verify if user is task owner
    try:
        
        task = Task.objects.get(id=pk)
        if task.created_by != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":        
        serializer = TaskDetailSerializer(task, many=False)
        return Response(serializer.data)
