from django.shortcuts import render


def payments_history(request):
    return render(request, 'payments.html')
