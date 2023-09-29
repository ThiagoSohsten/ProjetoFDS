from django import forms
from .models import CustomUser
from .models import Avaliacao


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

