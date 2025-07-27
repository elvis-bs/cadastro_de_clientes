from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from cadastro_cliente.models import Cliente, Endereco
from django.contrib.auth.models import User

# funcao para cadastrar usuarios do sistema
def cadastro_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario.html')
    else:   
        user = request.POST.get('usuario')
        senha = request.POST.get('password')

        usuario = User.objects.create_user(username=user, password=senha)
        usuario.save
        return HttpResponse ('OK')

# funcao para cadastrar clientes no sistema
def cadastro_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:   
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')

        cadastro = Cliente.objects.create(nome=nome, email=email, telefone=telefone, cpf=cpf)
        cadastro.save()
        return redirect('endereco', cadastro_id=cadastro.id)
        
# funcao para vincular o endereco do cliente cadastrado(na hora do cadastro)
def cadastro_endereco(request, cadastro_id):
    if request.method == 'GET':
        return render(request, 'endereco.html')
    else:
        cliente = Cliente.objects.get(id=cadastro_id)
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        estado = request.POST.get('estado')
        complemento = request.POST.get('complemento')
        rua = request.POST.get('rua')

        endereco = Endereco.objects.create(cliente=cliente, cep=cep, cidade=cidade, bairro=bairro, estado=estado, complemento=complemento, rua=rua)
        endereco.save()
        return render(request,'cadastro_cliente_finalizado.html')
    
def login(request):
    return render(request,'login.html')
    
