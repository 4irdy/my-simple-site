from django.shortcuts import render
from django.contrib import messages  # 👈 Add this line
from .forms import ContactForm

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Message:", form.cleaned_data['message'])
            messages.success(request, "Thanks for reaching out! Your message was received.")  # 👈 Add this line
            form = ContactForm()  # Resets form after submission
    return render(request, 'contact.html', {'form': form})

