from django.shortcuts import render


def index(request):
    return render(request, 'Home/homepage.html')


def dashboard(request):
    return render(request, 'Home/dashboard.html')


def category(request):
    return render(request, 'Home/category.html')


def jobs(request):
    return render(request, 'Home/jobs.html')
