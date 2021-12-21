from django.db import models

# Create your models here.
STATE_CHOICE = (
('punjab','punjab'), 
('KPK','KPK'),
('Gilgit','Gilgit'),
('Sind','Sind'),
('Balochistan','Balochistan'))
class Resumemodel(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    education = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    locality = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICE ,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=200)
    profile_img = models.ImageField(upload_to='profile_img',blank=True)
    my_file = models.FileField(upload_to="CV", blank=True)