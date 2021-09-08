from os import name
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register'),
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('tables/', tables, name='tables'),
    path('user-profile/', profile, name='profile'),
    path('qrcode/', qrcode, name='qrcode'),
    path('enviar-mensagem/', enviar_message, name='message'),
    path('registra-contatos/', contatos, name='contatos'),
    path('cadastrar-contato/', cadastrar_cotatos, name='cadastrar_cotatos'),

    #================ ERRORS ================ #

    path('error-500/', error_500, name='error_500'),
] 