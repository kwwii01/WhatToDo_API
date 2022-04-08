from django.http import JsonResponse

from tasks.models import Task, Status, Priority
from tasks.serializers import TaskListSerializer, StatusSerializer, PrioritySerializer


def status_list(request):
    """List all statuses"""
    if request.method == "GET":
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


def priority_list(request):
    """List all priorities"""
    if request.method == "GET":
        priorities = Priority.objects.all()
        serializer = PrioritySerializer(priorities, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


def task_list(request):
    """List all tasks"""
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
