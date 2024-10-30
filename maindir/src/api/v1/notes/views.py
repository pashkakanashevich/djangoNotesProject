from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Q

from apps.notes.models import Notes
from apps.notes.forms import NoteAddForm, NoteChangeForm
from importlib_metadata import files


# Create your views here.
def index(request):
    sort_by = request.POST.get('sort', 'created_at')

    search_query = request.GET.get('search', '')

    if search_query:
        notes = Notes.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        ).order_by(sort_by)
    else:
        notes = Notes.objects.all().order_by(sort_by)

    context = {
        'notes': notes,
        'sort': sort_by
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
        form = NoteAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
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
        form = NoteChangeForm(request.POST, instance=note, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteChangeForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})


