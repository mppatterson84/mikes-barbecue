from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from recipes.forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    paginate_by = 10
    ordering = ['-pk']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recipes'
        context['recipes_active'] = 'active'
        context['recipes_active_link'] = '#'
        context['recipes_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/recipe_new.html'
    form_class = RecipeForm
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Recipe'
        context['new_active'] = 'active'
        context['new_active_link'] = '#'
        context['new_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

    # https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_edit.html'
    form_class = RecipeForm
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_delete.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset

class RecipeSearchView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_search.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search Results'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                    Q(title__icontains=query) |
                    Q(body__icontains=query) 
                    ).distinct()
            if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
                queryset = queryset
            else:
                queryset = queryset.filter(published=True)
        else:
            queryset = None
        return queryset

class RecipeListAllView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list_all.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Recipes'
        context['all_active'] = 'active'
        context['all_active_link'] = '#'
        context['all_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset