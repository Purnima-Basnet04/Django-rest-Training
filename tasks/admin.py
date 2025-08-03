from django.contrib import admin
from . models import Task

admin.sites.register(Task)


