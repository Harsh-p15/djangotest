from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.
def signup(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if not username or not email or not pwd:
            return render( request, 'Signup.html', {
                'error':'please fill all fields'

            })
        
        if User.objects.filter(username=username).exists():
            return render( request, 'Signup.html',{
                'error':'username already exists'
                })
        
        my_user = User.objects.create_user(username,email,pwd)
        my_user.save()
        return redirect('login')

    return render( request,'Signup.html')

        #return redirect('login/')


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            return render( request, 'Login.html',{
                'error':'username doesnt exists, pls signup first'
                })

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('todo_list')
        else:
            return render(request, 'Login.html', {
                'error': 'invalid credentials'

            })
            
                                
    return render(request, 'Login.html')

def todo_list(request):
    todos = models.Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'todo_list.html',{'todos':todos })

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = models.Todo.objects.create(user=request.user, title=title, description= description)
        todo.save()
        return redirect('todo_list')
    
    return render(request, 'Add_todo.html')


def edit_todo(request, todo_id):
    todo = get_object_or_404(models.Todo, pk=todo_id, user = request.user)

    if request.method == 'POST':
        #todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo_list')

    return render(request, 'Edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
     todo = get_object_or_404(models.Todo, pk=todo_id, user = request.user)
     todo.delete()
     return redirect('todo_list')

def signout(request):
    logout(request)
    return redirect('login')

    