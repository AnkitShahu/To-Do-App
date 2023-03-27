from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
#from django.contrib.auth.forms import UserCreationForm
#from django.auth.models import User
from .forms import SignupForm
from django.contrib import messages

def task_list(request):
    if request.user.is_anonymous:
        return redirect('loginu')
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
        
    
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')


# Login view
# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('task_list')
#         else:
#             message = 'Invalid login credentials'
#     else:
#         message = ''
#     return render(request, 'login.html', {'message': message})

# Logout view
#@login_required
def user_logout(request):
    logout(request)
    return redirect('loginu')

def loginu(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

# def sign_up(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request, 'signup.html', {'form':fm})

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form':fm})