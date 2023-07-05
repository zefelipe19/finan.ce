from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from .models import Conta, Categoria
from django.db.models import Sum

from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'home.html', context)


def gerenciar(request):
    contas = Conta.objects.all()
    total_conta = contas.aggregate(Sum('valor'))['valor__sum']
    # total_conta = 0
    # for conta in contas:
    #     total_conta += conta.valor

    data = {'contas': contas, 'total_conta': total_conta}
    return render(request, 'gerenciar.html', context=data)


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
            return redirect(reverse_lazy('home:gerenciar'))

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
                             'Conta criada com sucesso!')
        return redirect(reverse_lazy('home:gerenciar'))
    elif request.method == 'GET':
        return redirect(reverse_lazy('home:gerenciar'))
