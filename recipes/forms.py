from django import forms
from recipes.models import Recipe
from ckeditor.widgets import CKEditorWidget

class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Recipe Title", 
                "class": "form-control"
            }
        )
    )

    body = forms.CharField(
        label='',
        required=True,
        widget=CKEditorWidget()
    )

    published = forms.CharField(
        label='Published',
        required=False,
        widget=forms.CheckboxInput()
    )
    
    class Meta:
        model = Recipe
        fields = [
            'title',
            'body',
            'published',
        ]