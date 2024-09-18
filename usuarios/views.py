from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.metohd == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
             if form["senha"].value() != form["repetir_senha"].value():
                return redirect('cadastro')
            
    return render(request, "usuarios/cadastro.html", {'form': form})