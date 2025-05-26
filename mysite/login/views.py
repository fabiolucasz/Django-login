from django.shortcuts import render

def home(request):
    return render(request, 'login/login.html')

def login(request):
    return render(request, 'login/login.html')

def cadastro(request):
    return render(request, 'login/cadastro.html')

def dashboard(request):
    return render(request, 'login/dashboard.html')

def profile(request):
    return render(request, 'login/profile.html')

def logout(request):
    return render(request, 'login/logout.html')

def password_recovery(request):
    return render(request, 'login/password_recovery.html')
