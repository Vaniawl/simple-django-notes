from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def hi(request):
    return HttpResponse("<h1>Hi</h1>")


def read_content(request):
    # Retrieving all notes from the database
    all_notes = Note.objects.all()
    return HttpResponse(all_notes)


def send_content(request):
    # creating a new Note Object
    new_note = Note(title='Codefinity')
    #saving the new note to the database

    new_note.save()
    return HttpResponse('Your note has been saved.')


# def update_content(request):
#     all_notes = Note.objects.all()
#     for note in all_notes:
#         note.title = 'My example title'
#         note.save()
#     return HttpResponse('Your note has been updated.')

def update_content(request):
    all_notes = Note.objects.all()
    for note in all_notes:
        note.title = 'LOL'
        note.save()
    return HttpResponse('Notes updated')


def delete_content(request):
    all_notes = Note.objects.all()
    for i in all_notes:
        i.delete()
    return HttpResponse('Notes deleted')


def special_page(request):
    return render(request, 'notes.html')

def your_view_function(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f"Title: {title}, Note text: {content}")
        new_note = Note(title=title, content=content)
        new_note.save()
        return redirect('notes')
    return render(request, 'notes.html')

# def index(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     notes = Note.objects.all().order_by('-id')
#     return render(request, 'notes.html', {'notes': notes})


def index(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm()

    notes = Note.objects.all().order_by('-id')
    return render(request, 'notes.html', {'form': form, 'notes': notes})


def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            note.title = title
            note.content = content
            note.save()
            return redirect('notes')

    return render(request, 'note_detail.html', {'note': note})

def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()

    notes = Note.objects.all().order_by('-id')
    render(request, 'notes.html', {'notes': notes})
    return redirect('/')