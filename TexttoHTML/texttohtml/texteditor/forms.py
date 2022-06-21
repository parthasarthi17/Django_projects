from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")

    class Meta:
        model=Editor
        fields="__all__"
