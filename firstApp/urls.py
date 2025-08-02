from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    FoodListView, FoodDetailView,
    ChefListView, ChefDetailView,
)

app_name = 'firstApp'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('foods/', FoodListView.as_view(), name='food_list'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('chefs/', ChefListView.as_view(), name='chef_list'),
    path('chef/<int:pk>/', ChefDetailView.as_view(), name='chef_detail'),
]