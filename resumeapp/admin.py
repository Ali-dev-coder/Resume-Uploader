from django.contrib import admin
from .models import Resumemodel
# Register your models here.

@admin.register(Resumemodel)

class Resumeadmin(admin.ModelAdmin):
    list_display = [ 'id','name','father_name',
    'dob',
    'education',
    'gender', 
    'city',
    'pin', 
    'locality',
    'state', 
    'mobile',
    'email',
    'job_city',
    'profile_img',
    'my_file']