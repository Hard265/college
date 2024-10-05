from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    return render(request, 'index.html')
