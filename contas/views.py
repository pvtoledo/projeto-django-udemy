import re
from django.db import transaction
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contas.models import Perfil
from contas.usuario_form import UserForm, PerfilForm


def validou_email(email):
    regex = '^(\w+)@[a-z]+(\.[a-z]+){1,2}$'

    if re.search(regex, email):
        return True
    else:
        return False


@transaction.atomic
def criar_conta(request):
    if request.method == 'POST':

        usuario = UserForm(request.POST)
        perfil = PerfilForm(request.POST, request.FILES)

        if perfil.is_valid() and usuario.is_valid():

            user = User.objects.create_user(
                first_name=usuario.cleaned_data['first_name'],
                last_name=usuario.cleaned_data['last_name'],
                username=usuario.cleaned_data['username'],
                email=usuario.cleaned_data['email'],
                password=usuario.cleaned_data['password'],
            )

            profile = Perfil(
                bio=perfil.cleaned_data['bio'],
                foto=perfil.cleaned_data['foto'],
                user=user,
            )

            profile.save()
            return redirect('login')
        else:
            return render(request, 'contas/criar_conta.html', {'form': usuario, 'form_perfil': perfil})
    else:
        return render(request, 'contas/criar_conta.html', {'form': UserForm(), 'form_perfil': PerfilForm()})


def htmx_valida_username(request):
    context = {'error_username': 'Nome de usuário indisponível', 'st_submit': 'disabled', 'cor': 'red'}
    username_param = request.POST.get('username')

    if not User.objects.filter(username=username_param):
        context['error_username'] = 'Nome de usuário disponível'
        context['cor'] = 'green'

    if PerfilForm(request.POST).is_valid():
        context['st_submit'] = ''

    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)


def htmx_valida_email(request):
    context = {'usr_email': '', 'st_submit': 'disabled', 'cor': 'red'}
    email_param = request.POST.get('email')

    if not validou_email(email_param):
        context['usr_email'] = 'Email inválido.'
    if User.objects.filter(email=email_param):
        context['usr_email'] = 'Email já cadastrado.'
    if PerfilForm(request.POST).is_valid():
        context['usr_email'] = ''
        context['st_submit'] = ''
    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)


def htmx_valida_senha(request):
    context = {'erro_senha': 'As senhas não coincidem', 'st_submit': 'disabled', 'cor': 'red'}
    confirmar_senha = request.POST.get('confirmar_senha')
    senha = request.POST.get('password')

    if confirmar_senha == senha and PerfilForm(request.POST).is_valid():
        context['erro_senha'] = ''
        context['st_submit'] = ''

    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)
