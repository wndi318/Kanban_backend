from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from kanban.board import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'contact', views.ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
