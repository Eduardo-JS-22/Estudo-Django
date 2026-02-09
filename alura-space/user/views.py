from django.shortcuts import render, redirect
from user.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            '''user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                return redirect('index')
            else:
                return redirect('login')'''
            
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return redirect('login')

    return render(request, 'user/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                messages.error(request, 'As senhas não coincidem.')
                return redirect('register')
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            if User.objects.filter(username=username).first():
                messages.error(request, 'O nome de usuário já está em uso.')
                return redirect('register')
                
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Registro realizado com sucesso! Faça login para continuar.')
            return redirect('login')

    return render(request, 'user/register.html', {'form': form})