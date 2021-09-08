import os 
from pathlib import Path
import pandas as pd
from .models import Contatos

class Excel():
    def __init__(self):
        self.caminho = Path(__file__).resolve().parent.parent

    def handle_uploaded_file(self, f):
        with open(str(self.caminho) + '/app/arquivos/empresa1/planilha.xlsx', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
               
    def ler_xls(self):
        filename = str(self.caminho) + '/app/arquivos/empresa1/planilha.xlsx'

        pf = pd.read_excel(filename) 
        
        lista_nomes = []
        for i in pf['nome']:
            lista_nomes.append(i)

        lista_numeros = []
        for i in pf['numero']:
            if i.__class__ is float:
                i = int(i)
    
            lista_numeros.append(i)
       
        return lista_nomes, lista_numeros

    def inserir_contatos(self, contatos):

        lista_nomes = contatos[0]
        lista_numeros = contatos[1]
        #print(lista_nomes, lista_numeros)
        for i, data in enumerate(lista_nomes):
            try:
                obj = Contatos.objects.get_or_create(nome=data, numero=lista_numeros[i])
            except Exception as e:
                print(e)