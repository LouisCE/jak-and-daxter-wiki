from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})
