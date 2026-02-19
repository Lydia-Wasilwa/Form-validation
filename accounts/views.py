from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Logic to save user goes here (e.g., User.objects.create_user(...))
            messages.success(request, 'Account created successfully!')
            form = RegistrationForm() # Reset form after success
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
