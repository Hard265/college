from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    if request.user.is_superuser:
        return redirect('/admin')

    context = {"profile": request.user.student_profile}

    return render(request, 'index.html', context=context)


def examination_results(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    return render(request, 'examination-results.html')
