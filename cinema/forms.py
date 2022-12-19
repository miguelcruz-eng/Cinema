from django import forms

from .models import Clientes
from .models import Ingressos

class ClientForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('id_cliente', 'i_tipo_cliente', 'nome', 'data_nascimento')

class IngressoForm(forms.ModelForm):

    class Meta:
        model = Ingressos
        fields = ('id' , 'sessao_id_ingresso', 'tipo_tingresso', 'cliente_id_ingresso', 'assento_ingresso')