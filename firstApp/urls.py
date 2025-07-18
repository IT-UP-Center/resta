from django.urls import path
from . import views

urlpatterns = [
    # === index всего CRUD-приложения ===
    path('', views.MainView.as_view(), name='crud-index'),
    ]