
from django.urls import path

from .notes.views import index, note, add_note, delete_note, edit_note

app_name = 'notes'
urlpatterns = [
    path('', index, name='index'),
    path('note/<int:note_id>', note, name="note"),
    path('add', add_note, name='add_note'),
    path('delete/<int:note_id>', delete_note, name='delete_note'),
    path('edit/<int:note_id>', edit_note, name='edit_note')
]
