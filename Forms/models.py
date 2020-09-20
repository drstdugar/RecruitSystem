from django.db import models


class Application(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.DateTimeField()
    resume = models.FileField(upload_to="resume/")