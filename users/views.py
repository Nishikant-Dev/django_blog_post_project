from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegistration


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creted for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistration()
    return render(request, 'users/registration.html', {'form': form})
