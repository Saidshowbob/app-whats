from os import name
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse

import requests
from .forms import LoginForm, SignUpForm, UploadForm
from .excel import Excel as ex
from .chatapi import CHATapi
from .models import *

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


def logout_user(request):
    logout(request)

    return redirect('/login/')

@login_required(login_url='/login/')
def home(request):
    
    return render(request, 'index.html', locals())

@login_required(login_url='/login/')
def tables(request):

    return render(request, 'tables.html', locals())

@login_required(login_url='/login/')
def profile(request):
    
    return render(request, 'profile.html', locals())

@login_required(login_url='/login/')
def qrcode(request):
    
    api = CHATapi()

    print(api.gerar_qrcode())

    return redirect('/')

@login_required(login_url='/login/')
def enviar_message(request):

    try:
        api = CHATapi()

        excel = ex()
    
        numeros = []

        obj = Contatos.objects.all()

        for i in obj:
            numeros.append(i.numero)

        if request.method == 'POST':
            message = request.POST.get('msg')
            for i in numeros: 
                api.send_message(i, message)
        
        messages.success(request, 'Mensagens enviadas com sucesso!')

        return redirect('/')
    except Exception as e:
        print('error', e)
        return error_500

@login_required(login_url='/login/')
def error_500(request):

    return render(request, 'page-500.html', locals())

@login_required(login_url='/login/')
def contatos(request):
    excel = ex()

    listas = excel.ler_xls()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES.get('arquivo')
            excel.handle_uploaded_file(arquivo)
            
            excel.inserir_contatos(listas)
    else:
        form = UploadForm() # A empty, unbound form
    return render(request, 'cadastrar_contato.html', locals())

@login_required(login_url='/login/')
def cadastrar_cotatos(request): 

    if request.method == 'POST':
        
        nome = request.POST.get('nome')

        numero = request.POST.get('numero')
        print(nome, numero)
        obj =  Contatos.objects.get_or_create(nome=nome, numero=numero)
        
        messages.success(request, 'Contato cadastrado com sucesso!')

        return redirect('/registra-contatos/')
    else:
        return redirect('/registra-contatos/')
# Create your views here.
