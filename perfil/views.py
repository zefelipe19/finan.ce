from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from .models import Conta, Categoria
from django.db.models import Sum
from .utils import calcula_total

from django.http import HttpResponse


def home(request):
    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')
    return render(request, 'home.html', {'contas': contas, 'total_contas': total_contas})


def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total_conta = calcula_total(contas, 'valor')
    return render(request, 'gerenciar.html', {
        'contas': contas,
        'total_conta': total_conta,
        'categorias': categorias
    })


def cadastrar_banco(request):
    if request.method == 'POST':
        apelido = request.POST.get('apelido')
        banco = request.POST.get('banco')
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        icone = request.FILES.get('icone')

        if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect(reverse_lazy('perfil:gerenciar'))

        conta = Conta(
            apelido=apelido,
            banco=banco,
            tipo=tipo,
            valor=valor,
            icone=icone
        )
        if conta:
            conta.save()
        messages.add_message(request, constants.SUCCESS,
                             f'Conta {conta.apelido} criada com sucesso!')
        return redirect(reverse_lazy('perfil:gerenciar'))
    elif request.method == 'GET':
        return redirect(reverse_lazy('perfil:gerenciar'))


def deletar_banco(request, id):
    conta = Conta.objects.filter(id=id).first()
    conta.delete()
    messages.add_message(request, constants.SUCCESS,
                         f'Conta {conta.apelido} deletada com sucesso!')
    return redirect(reverse_lazy('perfil:gerenciar'))


def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    if len(nome.strip()) > 0:
        categoria = Categoria(
            categoria=nome,
            essencial=essencial
        )
        if categoria:
            categoria.save()
            messages.add_message(
                request, constants.SUCCESS, f'A categoria {categoria.categoria} foi criada com sucesso!')
        else:
            messages.add_message(request, constants.ERROR,
                                 f'A categoria não pode ser criada!')
    else:
        messages.add_message(request, constants.ERROR,
                             f'Por favor, preencha o campo Categoria para criar uma.')
    return redirect(reverse_lazy('perfil:gerenciar'))


def update_categoria(request, id):
    categoria = Categoria.objects.filter(id=id).first()
    categoria.essencial = not categoria.essencial
    categoria.save()
    return redirect(reverse_lazy('perfil:gerenciar'))
