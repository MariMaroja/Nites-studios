from django.shortcuts import render, get_object_or_404, redirect
from apps.user.forms import LoginForms, Registerforms
from apps.employee.models import Identify
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            key = form['password'].value()

        user = auth.authenticate(
            request,
            username=name,
            password=key
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{name} successfully logged!')
            return redirect('index')
        else:
            messages.error(request, 'Error in login')
            return redirect('login')
    
    return render(request, 'user/login.html', {'form':form})

def register(request, identity_id):
    form = Registerforms()
    identify = get_object_or_404(Identify, pk=identity_id)

    if request.method == 'POST':
        form = Registerforms(request.POST)

        if form.is_valid():
            name=form['name_register'].value()
            email=form['email'].value()
            key=form['password_1'].value()
            identity=form['identity'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'User already exists!')
                return redirect('register')
            
            if identity not in identify:
                messages.error(request, 'Id not allowed!')
                return redirect('register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=key
            )
            user.save()
            messages.success(request, 'User successfully created!')
            return redirect('login')

def logout(request):
    auth.logout(request)
    messages.success(request, 'User logged out')
    return redirect('index')