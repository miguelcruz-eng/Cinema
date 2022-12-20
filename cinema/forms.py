from django import forms

from .models import Clientes
from .models import Ingressos
from .models import Pedidos
from .models import ItensPedido
from .models import Compras

class ClientForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('id_cliente', 'i_tipo_cliente', 'nome', 'data_nascimento')

class IngressoForm(forms.ModelForm):

    class Meta:
        model = Ingressos
        fields = ('id' , 'tipo_tingresso', 'cliente_id_ingresso', 'assento_ingresso')

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ('id' , 'cliente', 'data')

class IpedidosForm(forms.ModelForm):

    class Meta:
        model = ItensPedido
        fields = ('id' , 'pedido', 'produto', 'quantidade')

class PromoForm(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ('cliente',)