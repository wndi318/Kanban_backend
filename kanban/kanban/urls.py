from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from board.views import LoginView
from board import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'contact', views.ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('admin/', admin.site.urls),
]
