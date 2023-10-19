from django import forms
from .models import CustomUser
from .models import Avaliacao
from django import forms
from .models import Cartao

class CadastroCartaoForm(forms.ModelForm):
    numero = forms.CharField(label='Número do Cartão', max_length=16, widget=forms.TextInput(attrs={'placeholder': '1234 5678 9012 3456'}))
    validade = forms.DateField(label='Data de Validade', widget=forms.DateInput(attrs={'placeholder': 'MM/AAAA'}), input_formats=['%m/%Y'])
    cvv = forms.CharField(label='CVV', max_length=3, widget=forms.PasswordInput(attrs={'placeholder': '123'}))

    class Meta:
        model = Cartao
        fields = ['numero', 'validade', 'cvv']



class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

class NichoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nicho']
        


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['comentario']

