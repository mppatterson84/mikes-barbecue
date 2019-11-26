from .models import Recipe
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

class RecipeAdminForm(forms.ModelForm):
    body = forms.CharField(
        label='Recipe Body',
        required=True,
        widget=CKEditorWidget()
    )
    class Meta:
        model = Recipe
        fields = [
            'title',
            'body',
            'author',
            'created_at',
            'updated_at',
            'slug',
            'published',
        ]

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    readonly_fields = ('updated_at', 'slug')

admin.site.register(Recipe, RecipeAdmin)