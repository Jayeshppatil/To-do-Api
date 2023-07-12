from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='frontend:login')
def list(request):
    return render(request, 'frontend/list.html')



def registerPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Accounts was created for ' + username)

            return redirect('/')

    context = {'form':form}
    return render(request, 'frontend/register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'frontend/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('/')