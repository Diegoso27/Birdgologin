from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect

def home(request):
  return HttpResponseRedirect('')

def register_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if password==confirm_password:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'No es posible utilizar el nombre de usuario')
        return redirect('register')
      else:
        user = User.objects.create_user(
          username=username,
          password=password,
        )
        user.save()
          
        return redirect('login_user')
    else:
      messages.info(request, 'Las contraseñas no son iguales')
      return redirect('register')
  else:
    return render(request, 'registration/registration.html')

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('index')
    else:
        messages.info(request, 'Invalid Username or Password')
        return redirect('login_user')
        
  else:
      return render(request, 'registration/login.html')
  

def logout_user(request):
  auth.logout(request)
  return redirect('index')
