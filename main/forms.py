from django import forms
from .models import Note

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Note title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your note here...'}),
        }
