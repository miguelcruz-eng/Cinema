from django import forms

from .models import Clientes

class ClientForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('id_cliente', 'i_tipo_cliente', 'nome', 'data_nascimento')