from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, NichoForm, AvaliacaoForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemCarrinho 

def remove_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('carrinho')

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})




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

# ... suas importações ...

def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    carrinho_itens = [
        {'produto': Produto.objects.get(id=produto_id), 'quantidade': quantidade}
        for produto_id, quantidade in carrinho.items()
    ]
    total = sum(item['produto'].preco * item['quantidade'] for item in carrinho_itens)
    return render(request, 'loja/carrinho.html', {'carrinho_itens': carrinho_itens, 'total': total})

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(produto_id)] = carrinho.get(str(produto_id), 0) + 1  # Adiciona ou atualiza
    request.session['carrinho'] = carrinho
    return redirect('carrinho')

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]  # Remove se estiver no carrinho
    request.session['carrinho'] = carrinho
    return redirect('carrinho')



def confirmar_compra(request):
    request.session['carrinho'] = {}  # Limpa o carrinho
    return render(request, 'loja/compra_confirmada.html')
