from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        student = authenticate(user_id=user_id, password=password)

        if student is not None:
            auth_login(request, student)
            return redirect("index")
    return render(request, 'login.html')
