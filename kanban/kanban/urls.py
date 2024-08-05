from django.contrib import admin
from django.urls import path
from board.views import LoginView, ContactView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:pk>/', ContactView.as_view()),
    path('admin/', admin.site.urls),
]
