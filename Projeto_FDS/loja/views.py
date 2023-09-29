from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, NichoForm
from .models import Produto
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, NichoForm, AvaliacaoForm




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'loja/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')




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

# ... (Outras views e importações)

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})

def avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('home')
    else:
        form = AvaliacaoForm()
    return render(request, 'loja/avaliacao.html', {'form': form})

