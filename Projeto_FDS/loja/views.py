from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .forms import CustomUserCreationForm, NichoForm, AvaliacaoForm, CadastroCartaoForm 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ItemCarrinho, Produto, CustomUser, ItemPedido


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
    # Verificando se o usuário está autenticado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para confirmar a compra.')
        return redirect('login')  # Redirecionar para a página de login se o usuário não estiver autenticado

    if request.method == 'POST':
        form = CadastroCartaoForm(request.POST)
        if form.is_valid():
            # 1. Crie um novo pedido para o usuário atual
            carrinho = request.session.get('carrinho', {})
            carrinho_itens = [
                {'produto': Produto.objects.get(id=produto_id), 'quantidade': quantidade}
                for produto_id, quantidade in carrinho.items()
            ]
            total = sum(item['produto'].preco * item['quantidade'] for item in carrinho_itens)
            novo_pedido = Pedido.objects.create(usuario=request.user, total=total)
            
            # 2. Para cada item no carrinho, crie um ItemPedido.
            for item in carrinho_itens:
                ItemPedido.objects.create(
                    produto=item['produto'],
                    pedido=novo_pedido,
                    quantidade=item['quantidade']
                )
            
            # ... restante da lógica para salvar cartão ...

            # 3. Depois de criar todos os ItemPedido associados, limpe o carrinho.
            request.session['carrinho'] = {}
            
            return render(request, 'loja/compra_confirmada.html')
    else:
        form = CadastroCartaoForm()

    return render(request, 'loja/cadastro_cartao.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Pedido, Devolucao, Produto

def minhas_compras(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'loja/minhas_compras.html', {'pedidos': pedidos})


def iniciar_devolucao(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        produtos_a_devolver = request.POST.getlist('produtos_a_devolver')
        for produto_id in produtos_a_devolver:
            produto = Produto.objects.get(id=produto_id)
            Devolucao.objects.create(pedido=pedido, produto=produto)
        return redirect('especificar_motivo_devolucao', pedido_id=pedido_id)
    return render(request, 'loja/iniciar_devolucao.html', {'pedido': pedido})

def especificar_motivo_devolucao(request, pedido_id):
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        devolucoes = Devolucao.objects.filter(pedido__id=pedido_id)
        for devolucao in devolucoes:
            devolucao.motivo = motivo
            devolucao.save()
        return redirect('home')
    return render(request, 'loja/especificar_motivo.html')
