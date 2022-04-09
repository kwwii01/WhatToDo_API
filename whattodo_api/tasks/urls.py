from django.urls import path

from tasks import views


urlpatterns = [
    path('statuses/', view=views.status_list),
    path('priorities/', view=views.priority_list),
    path('tasks/', view=views.task_list),
    path('tasks/<str:pk>/', view=views.task_details),
]
