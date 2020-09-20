from django.shortcuts import render


def signup(request):
    return render(request, 'Register/signup_comp.html')
