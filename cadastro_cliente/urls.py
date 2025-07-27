
from django.urls import path
from .views import cadastro_cliente, cadastro_endereco, cadastro_usuario,login


urlpatterns = [
    
    #cadastro usuario do sistema
    path('cadastro_usuario/',cadastro_usuario, name='usuario'),
    #cadastro cliente
    path('cadastro_cliente/',cadastro_cliente, name='cadastro'),
    #cadastro do endereço vinculado ao cliente cadastrado
    path('cadastro_endereco/<int:cadastro_id>/',cadastro_endereco, name='endereco'),
    path('login/',login, name='login'),
    
]
