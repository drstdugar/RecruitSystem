from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Application


def apply(request):
    return render(request, 'Forms/apply.html')


def add_apply(request):
    fname = request.POST['fname']
    mname = request.POST['mname']
    lname = request.POST['lname']
    contact = request.POST['contact']
    address = request.POST['address']
    email = request.POST['email']
    gender = request.POST['gender']
    dob = request.POST['dob']
    resume = request.FILES['resume']

    Application.objects.create(fname=fname, mname=mname, lname=lname, contact=contact, address=address, email=email,
                         gender=gender, dob=dob, resume=resume)
    apply_info = Application.objects.all()

    return render(request, 'Forms/infoview.html', {'apply': apply_info})


def infoview(request):
    apply_info = Application.objects.all()

    return render(request, 'Forms/infoview.html', {'apply': apply_info})