from django.views.generic import ListView, DetailView, TemplateView
from .models import Category, Food, Chef

class CategoryListView(ListView):
    model = Category
    template_name = 'firstApp/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'firstApp/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = self.object.foods.all()
        return context

class FoodListView(TemplateView):
    template_name = 'firstApp/food_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # group foods by category
        context['categories'] = Category.objects.prefetch_related('foods').all()
        return context

class FoodDetailView(DetailView):
    model = Food
    template_name = 'firstApp/food_detail.html'
    context_object_name = 'food'

class ChefListView(ListView):
    model = Chef
    template_name = 'firstApp/chef_list.html'
    context_object_name = 'chefs'

class ChefDetailView(DetailView):
    model = Chef
    template_name = 'firstApp/chef_detail.html'
    context_object_name = 'chef'


class About(TemplateView):
    template_name = 'firstApp/about.html'
