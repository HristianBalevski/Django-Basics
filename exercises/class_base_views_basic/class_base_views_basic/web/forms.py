from django import forms

from class_base_views_basic.web.models import Todo


class TodoBaseForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
