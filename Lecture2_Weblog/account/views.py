from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User


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


def user_register(request):
    if request.method == 'POST':
        my_form = UserRegisterForm(request.POST)
        if my_form.is_valid():
            cd = my_form.cleaned_data
            User.objects.create(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'you registered successfully now you can log in', 'success')
            return redirect('account:login')
    else:
        my_form = UserRegisterForm()

    context = {
        'form': my_form
    }
    return render(request, 'account/register.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('account:login')
