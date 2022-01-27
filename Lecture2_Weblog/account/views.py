from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('post:home')
            else:
                messages.error(request, 'something went wrong please try again', 'warning')
                return redirect('account:login')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)








def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

    else:
        form = UserRegisterForm()



    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)
