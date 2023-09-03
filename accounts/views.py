from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

# Create your views here.
def login(request):
    register_form = RegistrationForm()
    login_form = LoginForm()
    if request.method == 'POST':
        form = request.POST.get('form_type')
        if form == 'register':
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                register = register_form.save(commit=False)
                full_name = register_form.cleaned_data['full_name'].split()
                register.first_name = full_name[0]
                register.last_name = full_name[1]
                register.set_password(register_form.cleaned_data['password'])
                register.save()
                messages.add_message(request, messages.SUCCESS, 'You have successfully registered!')
                return redirect(reverse_lazy('login'))
        elif form == 'login':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(email=login_form.cleaned_data['email'], password = login_form.cleaned_data['password'])
                if not user:
                    messages.add_message(request, messages.ERROR, 'Email and password does not match!')
                    return redirect(reverse_lazy('login'))
                django_login(request, user)
                return redirect(reverse_lazy('home'))
        return redirect(reverse_lazy('login'))
    context = {
        'register_form': register_form,
        'login_form': login_form
    }
    return render(request, 'login.html', context)

def my_account(request):
    return render(request, 'my-account.html')