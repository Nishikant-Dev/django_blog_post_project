from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creted!!You can login now!')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html');


def logout(request):
    django_logout(request)
    return redirect('login')
