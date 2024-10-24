# forms.py
from django import forms
from .models import Notes

class NoteAddForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название заметки'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите содержание заметки'}),
        }

class NoteChangeForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']


