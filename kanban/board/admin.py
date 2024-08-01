from django.contrib import admin
from .models import Task
from .models import Contact

admin.site.register(Task)
admin.site.register(Contact)
