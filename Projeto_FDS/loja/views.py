from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, NichoForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nicho')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def nicho(request):
    if request.method == 'POST':
        form = NichoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NichoForm()
    return render(request, 'nicho.html', {'form': form})

# Adicione sua view de login e home conforme necessário

# Create your views here.
