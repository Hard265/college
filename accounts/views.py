from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        student = authenticate(user_id=user_id, password=password)

        if student is not None:
            auth_login(request, student)
            return redirect("index")
    return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect("login")
    return render(request, 'logout.html')
