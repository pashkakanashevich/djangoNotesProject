from django import forms
from .models import Notes


class NoteAddForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'image', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название заметки'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите содержание заметки'}),
            'priority': forms.Select(choices=Notes.PRIORITY_CHOICES),
        }

    image = forms.ImageField(required=False)


class NoteChangeForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'image', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название заметки'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите содержание заметки'}),
            'priority': forms.Select(choices=Notes.PRIORITY_CHOICES),
        }

    image = forms.ImageField(required=False)
