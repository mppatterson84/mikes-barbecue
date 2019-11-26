from django.urls import path
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    RecipeCreateView, 
    RecipeUpdateView, 
    RecipeDeleteView, 
    RecipeListAllView,
    RecipeSearchView, 
)

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:pk>/<slug:slug>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name='recipe-new'),
    path('recipes/<int:pk>/<slug:slug>/edit/', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipes/<int:pk>/<slug:slug>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
    path('recipes/all/', RecipeListAllView.as_view(), name='recipe-list-all'),
]