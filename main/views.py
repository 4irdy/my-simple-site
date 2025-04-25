from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, NoteForm
from .models import Note

# Homepage View
def home_view(request):
    return render(request, 'home.html')

# About Page View
def about_view(request):
    return render(request, 'about.html')

# Contact Page View
def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Message:", form.cleaned_data['message'])
            messages.success(request, "Thanks for reaching out! Your message was received.")
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Note Views
@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note-list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note-list')
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note-list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
