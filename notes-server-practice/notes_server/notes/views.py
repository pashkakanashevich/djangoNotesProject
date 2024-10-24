from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from notes.models import Notes
from notes.forms import NoteAddForm, NoteChangeForm


# Create your views here.
def index(request):
    context = {
        'notes': Notes.objects.all()
    }
    return render(request, 'notes/index.html', context)

def note(request, note_id):
    if note_id:
        note = Notes.objects.get(id=note_id)
    else:
        note = None
    context = {
        'note': note,
    }

    return render(request, 'notes/note.html', context)

def add_note(request):
    if request.method == "POST":
        form = NoteAddForm(data=request.POST)
        if form.is_valid():  # Проверка на валидность формы
            form.save()  # Автоматически сохранит title и description
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteAddForm()

    context = {
        'form': form,
    }

    return render(request, 'notes/inputForm.html', context)

def delete_note(request, note_id):

    Notes.objects.get(id=note_id).delete()
    return HttpResponseRedirect(reverse("notes:index"))


def edit_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    if request.method == 'POST':
        form = NoteChangeForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteChangeForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})


