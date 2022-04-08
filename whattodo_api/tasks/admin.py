from django.contrib import admin

from .models import Status, Priority, Task


admin.site.register([Status, Priority, Task])
