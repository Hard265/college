from django.shortcuts import render, redirect
from .forms import CollegeUserLoginForm as LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {form: 'login_form'})
